"""
x
"""

import unittest
from dash_mantine_template.components.utils.QueryBuilder import QueryBuilder


class TestQueryBuilder(unittest.TestCase):

    def test_add_range_date_constraint_empty(self):
        qb = QueryBuilder(base_query="SELECT * FROM table")
        qb._add__range_date__constraint()
        self.assertEqual(qb.base_query, "SELECT * FROM table")
        self.assertEqual(qb.params, {})

    def test_add_range_date_constraint_with_range(self):
        qb = QueryBuilder(
            base_query="SELECT * FROM table",
            list_with_date_range=["2024-01-01", "2024-01-31"],
        )
        qb._add__range_date__constraint()
        self.assertIn("date__column between", qb.base_query)
        self.assertEqual(qb.params["start_date_"], "2024-01-01")
        self.assertEqual(qb.params["end_date_"], "2024-01-31")

    def test_add_individual_date_constraint_empty(self):
        qb = QueryBuilder(base_query="SELECT * FROM table")
        qb._add__individual_date__constraint()
        self.assertEqual(qb.base_query, "SELECT * FROM table")
        self.assertEqual(qb.params, {})

    def test_add_individual_date_constraint_with_dates(self):
        qb = QueryBuilder(
            base_query="SELECT * FROM table",
            list_with_individual_dates=["2024-01-01", "2024-01-02"],
        )
        # simulate attribute "transaction_date" (your code uses self.transaction_date)
        qb._add__individual_date__constraint()
        self.assertIn("date__column IN", qb.base_query)
        self.assertIn("individual_date__list_", qb.params)

    def test_add_multiselect_constraint_empty(self):
        qb = QueryBuilder(base_query="SELECT * FROM table")
        qb._add__multiselect__constraint()
        self.assertEqual(qb.base_query, "SELECT * FROM table")
        self.assertEqual(qb.params, {})

    def test_add_multiselect_constraint_with_values(self):
        qb = QueryBuilder(
            base_query="SELECT * FROM table",
            multi_select=["A", "B"],
        )
        qb._add__multiselect__constraint()
        self.assertIn("multiselect__column in", qb.base_query)
        self.assertIn("new_reopening__list_", qb.params)

    def test_add_range_slider_constraint_empty(self):
        qb = QueryBuilder(base_query="SELECT * FROM table")
        qb._add__range_slider__constraint()
        self.assertEqual(qb.base_query, "SELECT * FROM table")
        self.assertEqual(qb.params, {})

    def test_add_range_slider_constraint_with_values(self):
        qb = QueryBuilder(
            base_query="SELECT * FROM table",
            range_slider=[1, 10],
        )
        qb._add__range_slider__constraint()
        self.assertIn("range__column", qb.base_query)
        self.assertEqual(qb.params["min_range_slider_"], "1")
        self.assertEqual(qb.params["max_range_slider_"], "10")

    def test_create_dynamic_query_with_all_filters(self):
        qb = QueryBuilder(
            base_query="SELECT * FROM table WHERE 1=1",
            list_with_date_range=["2024-01-01", "2024-01-31"],
            list_with_individual_dates=["2024-01-05"],
            multi_select=["X"],
            range_slider=[5, 15],
        )
        qb.create_dynamic_query()
        # All constraints should be applied
        self.assertIn("date__column between", qb.base_query)
        self.assertIn("date__column IN", qb.base_query)
        self.assertIn("multiselect__column in", qb.base_query)
        self.assertIn("range__column", qb.base_query)
        self.assertGreater(len(qb.params), 0)

    def test_group_by_part(self):
        qb = QueryBuilder(
            base_query="SELECT col FROM table",
            group_by_part_of_query="GROUP BY col",
        )
        qb.add_group_by_part()
        self.assertIn("GROUP BY col", qb.base_query)

    def test_get_final_query_and_params(self):
        qb = QueryBuilder(base_query="SELECT 1", params={"a": 1})
        self.assertEqual(qb.get_final_parametrized_query(), "SELECT 1")
        self.assertEqual(qb.get_final_parameters(), {"a": 1})



