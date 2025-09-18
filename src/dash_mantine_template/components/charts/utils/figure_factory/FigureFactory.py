"""
Idea of this file is to have template class for
creating Plotly figures.

There should be methods to adjust chart's
appearance.

This class will be used inside callback.


Features present ATM:

    - get_data() --> logic for getting data is put here

    - prepare_date() --> Data manipulation is done here. Prepare data for plotting.

    - create_chart() --> Chart is created here.

    - apply_styles() --> Styling of chart is done here. It is 'main-like' function.
                        All styling-like methods are called here.

    - set_theme() --> Setting background of chart dark or light.

    - get_figure() --> Method to get final Plotly figure. Output should be returned as
                        callback output.

    - set_color__paper_bg() --> Setting color to element of Plotly figure.

    - set_color__plot_bg() --> Setting color to element of Plotly figure.

    - set_title() --> Set title of Plotly figure.

    - set_axis_label() --> Set names of chart axis.

    - set_margin() --> Setting margin of Plotly figure.

    - set_plot_outline() --> Used to put square box around Plotly figure.

    - set_gridlines() --> Setting gridlines (horizontal and vertical) visible.

    - set_gridlines_color() --> Setting gridlines color.

    - set_gridlines_width() --> Setting thickness of gridlines.

    - set_zero_lines() --> Setting color of vertical/horizontal lines at x/y=0.
                            This is setting only color that is in line with
                            background color of chart.
                            User can set specific color or use default one.

    - set_xaxis_rotation() --> Purpose of this function is to rotate values
                                that are shown on X axis.

    - set_axis_label_color() --> Set the color of values that are present on
                                X and Y axis (NOT for axis names).

    - set_axis_name_color() --> Set color of axis names (NOT color of values
                                shown on axis).

    - set_logarithmic_scale() --> Used to set X or Y axis to be of logarithmic
                                    scale.

    - set_legend_position() --> Legend can be located on top or on bottom of
                                the chart.

    - set_font_style() --> Used to set font type/style for words written on
                            Plotly chart.

    - set_yaxis_spacing() --> Used to determine space between vertical axis
                            and values on Y axis.
                            It makes values on Y axis look not so close to
                            vertical axis (Y axis).

    - set_yaxis_value_style() --> Values on Y axis could be in 'K' notation (6k)
                                or they could be written with with zeros (6000).


Planned features:
    - set_ticks() --> Purpose of this function is to set small horizontal/vertical
                    dash-es next to value on X and Y axis.
                    Those dash-es can help better see where is invisible line for
                    each value on X or Y axis.

"""

from typing import Optional

import pandas as pd
import plotly.graph_objects as go
from pydantic import ConfigDict, validate_call

from dash_mantine_template.components.charts.utils.figure_factory.FigureFactory__types import (
    BackgroundColor,
    Figure,
    LegendPosition,
    ValueStyle,
)


class FigureFactory:
    """
    Following two methods should be done first.

    They will create Plotly figure object that
    will hold styles and attributes that are
    going to be updated by other methods of
    this class.

    Tips: How to find all attributes of Plotly.Figure()
    object that can be updated in .update_layout() method?
        --> Link to Plotly.Figure() documentation:
            https://plotly.com/python/reference/layout/
        --> All possible options to customize Plotly chart
            can be found by exploring GraphObject library.
            Example:
                    self.figure.value.update_layout({
                        "xaxis_title": go.layout.xaxis.Title(text=x_axis_name),
                        "yaxis_title": go.layout.yaxis.Title(text=y_axis_name)
                })
            We can see pattern here:
                Key is named with underscore...
                Value comes from Plotly.go library...
    """

    figure: Figure
    raw_df: pd.DataFrame

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def __init__(self, background_color: BackgroundColor):
        """
        This function is used to initiate class with (all) parameters
        that will be used along the way i.e. in methods of this class.


        Here is example of how additional data can be provided in
        __init__ method. We can see that now additional parameters
        are required: x_data, y_data.

            @validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
            def __init__(self, background_color: BackgroundColor, x_data: list, y_data: list):
                super().__init__(background_color=background_color)
                self.x_data = x_data
                self.y_data = y_data

        """
        self.background_color = BackgroundColor(value=background_color)

    def get_data(self):
        """
        Purpose of this function is to get data from
        database i.e. to run queries.

        """
        pass

    def import_data(self, df: pd.DataFrame):
        """
        This method should be overwritten when
        children class is created from parent class.

        This method is used to import data into
        class/object instead of running query
        against sql table.

        Use case:
            - When there is several charts that are
            using same dataset.
            - Grouped and stacked bar charts. Same
            underlying data, different charts.

        """
        self.raw_df = df

    def export_data(self):
        """
        This method should be overwritten when
        children class is created from parent class.

        Purpose of this method is to export data
        that are already queried from database so
        that it can be used to create other types
        of charts.

        """
        return self.raw_df

    def prepare_data(self):
        """
        This method should be overwritten when
        children class is created from parent class.

        """
        pass

    def create_chart(self):
        """
        This method should be overwritten when
        children class is created from parent class.

        Following code snippet should be executed in this method.
        After chart is created, it should be saved in proper attribute
        so that styles can be applied onto it. Method self.apply_styles()
        will apply styles to self.Figure() object.

            self.figure = Figure(
                value=go.Figure(data=go.Scatter(x=self.x_data, y=self.y_data))
            )

        """
        pass

    def apply_styles(self):
        """
        Purpose of this function is to set configuration
        that were organized through methods.

        In order to have all configurations defined in
        one place.

        This method will apply styles to Plotly figure
        object that is stored in attribute self.Figure().

        """
        pass

    def set_theme(self):
        """
        Purpose of this function is set theme of Plotly
        chart.

        It is setting general theme of Plotly chart, but
        additional properties will be changed in subsequent
        methods.

        """

        if self.background_color.value == "dark":
            self.figure.value.update_layout(template="plotly_dark")

        if self.background_color.value == "light":
            self.figure.value.update_layout(template="simple_white")

    def get_figure(self):
        """
        Purpose of this method is to return Plotly figure object
        that will be returned to user's browser in a callback.

        """
        return self.figure.value

    def set_color__paper_bg(self):
        """
        Purpose of this function is to set color
        of paper_bgcolor component of Plotly figure object.

        Component paper_bgcolor is part of figure object,
        but it is NOT core part.

        Here we can see difference between paper_bgcolor
        and plot_bgcolor components:

            - https://github.com/plotly/plotly.py/issues/1161
            - https://github.com/plotly/plotly.js/issues/2408

        """

        if self.background_color == "dark":
            self.figure.value.update_layout({"paper_bgcolor": "#1a1e28"})

        if self.background_color == "light":
            self.figure.value.update_layout({"paper_bgcolor": "rgb(255,255,255)"})

    def set_color__plot_bg(self):
        """
        Purpose of this function is to set color
        of paper_bgcolor component of Plotly figure.

        Is core/main part of figure object.

        Here we can see difference between paper_bgcolor
        and plot_bgcolor components:

            - https://github.com/plotly/plotly.py/issues/1161
            - https://github.com/plotly/plotly.js/issues/2408

        """

        if self.background_color == "dark":
            self.figure.value.update_layout({"plot_bgcolor": "#1a1e28"})

        if self.background_color == "light":
            self.figure.value.update_layout({"plot_bgcolor": "rgb(255,255,255)"})

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_title(
        self,
        title_text: str,
        subtitle_text: Optional[str] = None,
        font_size: Optional[int] = None,
        font_weight: Optional[int] = None,
    ):
        """
        Purpose of this method is to set everything
        related to title component of figure object.

        """
        self.figure.value.update_layout(
            title=dict(
                text=title_text,
                font=dict(size=font_size, weight=font_weight),
                pad=dict(b=0, l=0, r=0, t=0),
                subtitle=dict(text=subtitle_text),
            ),
            # It could have values between 0 and 1.
            # 0.5 means title will be horizontally
            # centered.
            title_x=0.015,
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_axis_label(
        self, x_axis_name: Optional[str] = None, y_axis_name: Optional[str] = None
    ):
        """
        Purpose of this method is to set names of X and Y axis.

        """

        self.figure.value.update_layout(
            {
                "xaxis_title": go.layout.xaxis.Title(text=x_axis_name),
                "yaxis_title": go.layout.yaxis.Title(text=y_axis_name),
            }
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_margin(self, left: int = 0, right: int = 0, top: int = 0, bottom: int = 0):
        """
        Purpose of this function is to set margin around
        Plotly figure.

        4 margins can be configured:
            Left
            Right
            Top
            Bottom

        """

        self.figure.value.update_layout(
            {"margin": go.layout.Margin(l=left, r=right, t=top, b=bottom)}
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_plot_outline(self, color: Optional[str] = None, line_width: float = 1):
        """
        Purpose of this method is to make
        chart to be put in a rectangular
        box.

        Rectangle color should depend on
        background color.

            - For white background, it should
            be black.

            - For dark background, it should
            be white.

        """
        if color is None and self.background_color.value == "dark":
            color = "white"

        elif color is None and self.background_color.value == "light":
            color = "black"

        self.figure.value.update_xaxes(
            showline=True, linewidth=line_width, linecolor=color, mirror=True
        )
        self.figure.value.update_yaxes(
            showline=True, linewidth=line_width, linecolor=color, mirror=True
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_gridlines(self, vertical: bool = False, horizontal: bool = False):
        """
        Purpose of this method is to show or
        hide, both, horizontal and vertical
        gridlines.

        """

        self.figure.value.update_layout(
            {"xaxis_showgrid": vertical, "yaxis_showgrid": horizontal}
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_gridlines_color(self, color: str):
        """
        TODO:

        """

        self.figure.value.update_layout(
            yaxis=dict(
                gridcolor=color,  # Change this to your desired color
            )
        )

        self.figure.value.update_layout(
            xaxis=dict(
                gridcolor=color,  # Change this to your desired color
            )
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_gridlines_width(self, thickness: float):
        """
        TODO:

        """
        self.figure.value.update_layout(
            yaxis=dict(
                gridwidth=thickness  # Adjust this to your desired thickness
            )
        )

        self.figure.value.update_layout(
            xaxis=dict(
                gridwidth=thickness  # Adjust this to your desired thickness
            )
        )

    def set_ticks(self, x_axis: bool, y_axis: bool):
        """
        TODO:

        """
        pass

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_zero_lines(
        self,
        color: Optional[str] = None,
        line_width: float = 1,
        show_x_axis_zeroline: Optional[bool] = None,
        show_y_axis_zeroline: Optional[bool] = None,
    ):
        """
        Purpose of this method is to set zero lines
        for both axis.

        Zero line is (vertical/horizontal) line that
        has value of 0.

        It makes chart look more appealing.

        """

        if color is None and self.background_color.value == "dark":
            color = "white"

        elif color is None and self.background_color.value == "light":
            color = "black"

        self.figure.value.update_xaxes(
            showline=show_x_axis_zeroline, linewidth=line_width, linecolor=color
        )

        self.figure.value.update_yaxes(
            showline=show_y_axis_zeroline, linewidth=line_width, linecolor=color
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_xaxis_rotation(self, degree: int):
        """
        Purpose of this function is to rotate values that are
        present on X axis.

        Parameters:
            degree - can be positive or negative.

        Rotation can be done around left or right
        side of objects that rotates. This is
        difficult to explain, try and see how it
        behaves.

        """

        self.figure.value.update_layout(
            xaxis=dict(tickangle=degree)  # Rotate x-axis labels by 45 degrees
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_axis_label_color(
        self,
        x_axis_label_color: Optional[str] = None,
        y_axis_label_color: Optional[str] = None,
    ):
        """
        Purpose of this method is to set color of values
        that are present on X and Y axis.

        It is NOT for axis names.

        For example, it will color values on X axis
        1,2,3,4,5 into desired color.

        """

        if x_axis_label_color is not None:
            self.figure.value.update_layout(
                xaxis=dict(color=x_axis_label_color)  # Set the color of the x-axis
            )

        if y_axis_label_color is not None:
            self.figure.value.update_layout(
                yaxis=dict(color=y_axis_label_color)  # Set the color of the x-axis
            )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_axis_name_color(
        self, x_axis_color: Optional[str] = None, y_axis_color: Optional[str] = None
    ):
        """
        Purpose of this method is to color NAMES
        of X and Y axis.

        I.e. it is setting color of titles of
        X and Y axis.

        It is NOT for coloring values present on
        axis.

        """

        if x_axis_color is not None:
            self.figure.value.update_layout(
                xaxis=dict(
                    title=dict(
                        font=dict(
                            color=x_axis_color  # Set the color of the x-axis title to red
                        )
                    )
                )
            )

        if y_axis_color is not None:
            self.figure.value.update_layout(
                yaxis=dict(
                    title=dict(
                        font=dict(
                            color=y_axis_color  # Set the color of the y-axis title to red
                        )
                    )
                )
            )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_axis_zeroline_color(
        self,
        x_zeroline_color: Optional[str] = None,
        y_zeroline_color: Optional[str] = None,
    ):
        """
        Purpose of this function is to set color
        of zero lines.

        This method is deprecated. Use set_zero_lines()
        instead.

        """

        self.figure.value.update_xaxes(zerolinecolor=x_zeroline_color)

        self.figure.value.update_yaxes(zerolinecolor=y_zeroline_color)

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_logarithmic_scale(self, y_axis: bool = False, x_axis: bool = False):
        """
        Purpose of this function is to set logarithmic scale
        for both axis.

        """

        if x_axis:
            self.figure.value.update_xaxes(type="log")

        if y_axis:
            self.figure.value.update_yaxes(type="log")

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_legend_position(self, position: LegendPosition):
        """
        Purpose of this method is to set position of
        legend on chart.

        Position can be TOP or BOTTOM.

        If this method is not called, then position
        would be default.

        """

        if position == LegendPosition.TOP:
            self.figure.value.update_layout(
                legend=dict(
                    orientation="v",
                    yanchor="top",
                    xanchor="right",
                    # 4th number in RGB is for transparency
                    bgcolor="rgba(255, 255, 255, 0)",
                )
            )

        if position == LegendPosition.BOTTOM:
            self.figure.value.update_layout(
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    # 4th number in RGB is for transparency
                    bgcolor="rgba(255, 255, 255, 0)",
                )
            )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_font_style(self, font_type: str, font_size: Optional[int] = None):
        """
        Purpose of this function is to set font family and
        font size.

        Styling is done for each part of chart:
            - General font family and font size
            - Hover label i.e. tooltip
            - Legend
            - X axis
                - Label
                - Tick font
            - Y axis
                - Label
                - Tick font
        """
        self.figure.value.update_layout(
            # For axis
            font=dict(
                family=font_type,
                size=font_size,
                weight=1,
            ),
            # For tooltip
            hoverlabel=dict(font=dict(family=font_type, size=font_size)),
            # For legend
            legend=dict(font=dict(family=font_type, size=font_size, weight=1)),
            # For X axis
            xaxis=dict(
                title=dict(font=dict(family=font_type, size=font_size, weight=1)),
                tickfont=dict(family=font_type, size=14, weight=1),
            ),
            # For Y axis
            yaxis=dict(
                title=dict(font=dict(family=font_type, size=font_size, weight=1)),
                tickfont=dict(family=font_type, size=14, weight=1),
            ),
        )

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_yaxis_spacing(self, number_of_spaces: Optional[int] = None):
        """
        Purpose of this function is to set spacing between
        values on Y axis and vertical zero line.

        Unit of measurement is SPACE.
        It will increase by number of SPACEs.

        """

        self.figure.value.update_yaxes(ticksuffix=number_of_spaces * " ")

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_yaxis_value_style(self, style: ValueStyle):
        """
        Purpose of this method is to set style of
        values that are shown on Y axis.

        15k VS 15,000 type of styles.

        """

        if style == ValueStyle.THOUSANDS:
            # Update layout to format Y-axis values with commas
            self.figure.value.update_yaxes(tickformat=",.0f")

        if style == ValueStyle.K_NOTATION:
            # Format values with K
            self.figure.value.update_yaxes(tickformat="~s")
