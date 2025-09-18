"""Builds the SQL queries based on the filters values"""

from typing import List, Optional

from pydantic import BaseModel


class QueryBuilder(BaseModel):
    """Dynamic query builder"""

    base_query: str
    group_by_part_of_query: Optional[str] = None
    params: dict = {}

    ### ### ### Filters ### ### ###

    # Date List # ---------- # ---------- #
    list_with_individual_dates: List[Optional[str]] = None

    # Date Range # ---------- # ---------- #
    list_with_date_range: List[Optional[str]] = None

    # Multiselect # ---------- # ---------- #
    multi_select: Optional[List[str]] = None

    # Range Slider # ---------- # ---------- #
    range_slider: Optional[List[int | float | str]] = None

    # Purpose of this is to help with structuring SQL query. How?
    # When we have list of values that should be filtered, we
    # use IN operator. For example, ...where col_1 IN (1,2,3,4).
    # What would happen if tuple has only one element? Then, it
    # would look like (7,). And this trailing comma would make
    # SQL syntax error.
    # Solution: Append some random thing to list. Make sure that
    # that added thing will never exist in database. So, our
    # example would look like (7, 111111111111111111111111) and
    # it will not mean SQL error.
    tuple_constant: list = ("111111",)

    def get_list(self):
        """
        x
        """
        return list(self.tuple_constant)

    def create_dynamic_query(self):
        """
        x
        """

        # Date Range
        self._add__range_date__constraint()

        # Date List
        self._add__individual_date__constraint()

        # Multiselect
        self._add__multiselect__constraint()

        # Range Slider
        self._add__range_slider__constraint()

    def add_group_by_part(self):
        """
        x
        """
        self.base_query += f"  {self.group_by_part_of_query}  "

    def get_final_parametrized_query(self):
        """
        x
        """
        return self.base_query

    def get_final_parameters(self):
        """
        x
        """
        return self.params

    def _add__individual_date__constraint(self):
        # When users open browser first time, before he/she clicks on calendar, it will
        # not have any values. So, input will be empty list.
        # We do not want to add additional constraints to query if user haven't selected
        # any dates yet.
        # This will be typical case for initial callback i.e. for first load of page.
        if (
            self.list_with_individual_dates is not None
            and len(self.list_with_individual_dates) > 0
        ):
            individual_date__list = tuple(
                self.list_with_individual_dates + self.get_list()
            ).__str__()
            self.base_query += " AND date__column IN :individual_date__list_"
            self.params["individual_date__list_"] = individual_date__list

    def _add__range_date__constraint(self):
        # When users open browser first time, before he/she clicks on calendar, it will
        # not have any values. So, input will be empty list.
        # We do not want to add additional constraints to query if user haven't selected
        # any dates yet.
        # This will be typical case for initial callback i.e. for first load of page.
        if self.list_with_date_range is not None and len(self.list_with_date_range) > 0:
            start_date = self.list_with_date_range[0]
            end_date = self.list_with_date_range[1]

            # if there is only one date selected,
            # end_date will be None
            if end_date is not None:
                self.base_query += (
                    " AND (date__column between :start_date_ and :end_date_ )"
                )
                self.params["start_date_"] = start_date
                self.params["end_date_"] = end_date

    def _add__multiselect__constraint(self):
        # When users open browser first time, before he/she clicks on calendar, it will
        # not have any values. So, input will be empty list.
        # We do not want to add additional constraints to query if user haven't selected
        # any dates yet.
        # This will be typical case for initial callback i.e. for first load of page.
        if self.multi_select is not None and len(self.multi_select) > 0:
            multiselect__list = tuple(self.multi_select + self.get_list()).__str__()
            self.base_query += " AND (multiselect__column in :new_reopening__list_)"
            self.params["new_reopening__list_"] = multiselect__list

    def _add__range_slider__constraint(self):
        # When users open browser first time, before he/she clicks on calendar, it will
        # not have any values. So, input will be empty list.
        # We do not want to add additional constraints to query if user haven't selected
        # any dates yet.
        # This will be typical case for initial callback i.e. for first load of page.
        if self.range_slider is not None and self.range_slider != []:
            self.range_slider = [str(val) for val in self.range_slider]
            min_range_slider = self.range_slider[0]
            max_range_slider = self.range_slider[1]
            self.base_query += " AND (cast(range__column as float) between :min_range_slider_ and :max_range_slider_)"
            self.params["min_range_slider_"] = min_range_slider
            self.params["max_range_slider_"] = max_range_slider
