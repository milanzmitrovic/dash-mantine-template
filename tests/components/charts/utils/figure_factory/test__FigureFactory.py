### ### ### Test FigureFactory ### ### ###


""" """

import plotly.graph_objects as go
import pytest

from dash_mantine_template.components.charts.utils.figure_factory.FigureFactory import (
    FigureFactory,
)
from dash_mantine_template.components.charts.utils.figure_factory.FigureFactory__types import (
    BackgroundColor,
    Figure,
    LegendPosition,
    ValueStyle,
)


@pytest.fixture
def figure_factory():
    """
    x
    """

    figure_factory = FigureFactory(background_color=BackgroundColor.dark.value)

    # Sample data
    x = [1, 2, 3, 4]
    y = [10, 15, 13, 17]

    # Create figure object.
    # In real usage of template, figure
    # object is created in create_chart()
    # method.
    figure_factory.figure = Figure(
        value=go.Figure(data=[go.Scatter(x=x, y=y, mode="lines", name="Line Chart")])
    )

    return figure_factory


def test_init(figure_factory):
    assert figure_factory.background_color == "dark"


def test_get_data(figure_factory):
    pass


def test_prepare_data(figure_factory):
    pass


def test_create_chart(figure_factory):
    pass


def test_apply_styles(figure_factory):
    pass


def test_set_theme_dark(figure_factory):
    """
    There is no easy way to check template
    that is set with this method:
        self.figure.value.update_layout(template="plotly_dark")

    So, we are using one trick. We know that when template is
    set to 'plotly_dark', paper_bgcolor will have value
    'rgb(17,17,17)'. So, we are going to check that value in test.

    """

    figure_factory.background_color = BackgroundColor.dark

    figure_factory.set_theme()

    assert (
        figure_factory.figure.value.layout.template.layout.paper_bgcolor
        == "rgb(17,17,17)"
    )


def test_set_theme_light(figure_factory):
    """
    There is no easy way to check template
    that is set with this method:
        self.figure.value.update_layout(template="light")

    So, we are using one trick. We know that when template is
    set to 'light', paper_bgcolor will have value 'white'. So,
    we are going to check that value in test.

    """

    figure_factory.background_color = BackgroundColor.light

    figure_factory.set_theme()

    assert figure_factory.figure.value.layout.template.layout.paper_bgcolor == "white"


def test_get_figure(figure_factory):
    assert isinstance(figure_factory.figure.value, go.Figure)

    assert figure_factory.figure.value.data[0].figure.data[0].x == (1, 2, 3, 4)

    assert figure_factory.figure.value.data[0].figure.data[0].y == (10, 15, 13, 17)


def test_set_color__paper_bg_dark(figure_factory):
    figure_factory.background_color = BackgroundColor.dark.value

    figure_factory.set_color__paper_bg()

    assert figure_factory.figure.value.layout.paper_bgcolor == "#1a1e28"


def test_set_color__paper_bg_light(figure_factory):
    figure_factory.background_color = BackgroundColor.light.value

    figure_factory.set_color__paper_bg()

    assert figure_factory.figure.value.layout.paper_bgcolor == "rgb(255,255,255)"


def test_set_color__plot_bg_dark(figure_factory):
    figure_factory.background_color = BackgroundColor.dark

    figure_factory.set_color__plot_bg()

    assert figure_factory.figure.value.layout.plot_bgcolor == "#1a1e28"


def test_set_color__plot_bg_light(figure_factory):
    figure_factory.background_color = BackgroundColor.light

    figure_factory.set_color__plot_bg()

    assert figure_factory.figure.value.layout.plot_bgcolor == "rgb(255,255,255)"


def test_set_title(figure_factory):
    figure_factory.set_title(
        title_text="title_text",
        subtitle_text="subtitle_text",
        font_size=11,
        font_weight=33,
    )

    assert figure_factory.figure.value.layout.title.text == "title_text"
    assert figure_factory.figure.value.layout.title.subtitle.text == "subtitle_text"
    assert figure_factory.figure.value.layout.title.font.size == 11
    assert figure_factory.figure.value.layout.title.font.weight == 33


def test_set_axis_label(figure_factory):
    figure_factory.set_axis_label(x_axis_name="x_axis_name", y_axis_name="y_axis_name")

    assert figure_factory.figure.value.layout.xaxis.title.text == "x_axis_name"
    assert figure_factory.figure.value.layout.yaxis.title.text == "y_axis_name"


def test_set_margin(figure_factory):
    figure_factory.set_margin(left=1, right=2, top=3, bottom=4)

    assert figure_factory.figure.value.layout.margin.l == 1
    assert figure_factory.figure.value.layout.margin.r == 2
    assert figure_factory.figure.value.layout.margin.t == 3
    assert figure_factory.figure.value.layout.margin.b == 4


def test_set_plot_outline(figure_factory):
    figure_factory.set_plot_outline(color="green", line_width=3)

    assert figure_factory.figure.value.layout.xaxis.showline is True
    assert figure_factory.figure.value.layout.yaxis.showline is True

    assert figure_factory.figure.value.layout.xaxis.linewidth == 3
    assert figure_factory.figure.value.layout.yaxis.linewidth == 3

    assert figure_factory.figure.value.layout.xaxis.mirror is True
    assert figure_factory.figure.value.layout.yaxis.mirror is True

    assert figure_factory.figure.value.layout.xaxis.linecolor == "green"
    assert figure_factory.figure.value.layout.yaxis.linecolor == "green"


def test_set_plot_outline_dark(figure_factory):
    figure_factory.background_color = BackgroundColor.dark

    figure_factory.set_plot_outline(color=None, line_width=3)

    assert figure_factory.figure.value.layout.xaxis.showline is True
    assert figure_factory.figure.value.layout.yaxis.showline is True

    assert figure_factory.figure.value.layout.xaxis.linewidth == 3
    assert figure_factory.figure.value.layout.yaxis.linewidth == 3

    assert figure_factory.figure.value.layout.xaxis.mirror is True
    assert figure_factory.figure.value.layout.yaxis.mirror is True

    assert figure_factory.figure.value.layout.xaxis.linecolor == "white"
    assert figure_factory.figure.value.layout.yaxis.linecolor == "white"


def test_set_plot_outline_light(figure_factory):
    figure_factory.background_color = BackgroundColor.light

    figure_factory.set_plot_outline(color=None, line_width=3)

    assert figure_factory.figure.value.layout.xaxis.showline is True
    assert figure_factory.figure.value.layout.yaxis.showline is True

    assert figure_factory.figure.value.layout.xaxis.linewidth == 3
    assert figure_factory.figure.value.layout.yaxis.linewidth == 3

    assert figure_factory.figure.value.layout.xaxis.mirror is True
    assert figure_factory.figure.value.layout.yaxis.mirror is True

    assert figure_factory.figure.value.layout.xaxis.linecolor == "black"
    assert figure_factory.figure.value.layout.yaxis.linecolor == "black"


def test_set_gridlines(figure_factory):
    figure_factory.set_gridlines(horizontal=True, vertical=True)

    assert figure_factory.figure.value.layout.xaxis.showgrid is True
    assert figure_factory.figure.value.layout.yaxis.showgrid is True


def test_set_gridlines_color(figure_factory):
    """
    TODO:

    """
    pass


def test_set_gridlines_width(figure_factory):
    """
    TODO:

    """
    pass


def test_set_ticks(figure_factory):
    """
    TODO:

    """
    pass


def test_set_zero_lines(figure_factory):
    figure_factory.set_zero_lines(
        color="green",
        line_width=11,
        show_x_axis_zeroline=True,
        show_y_axis_zeroline=True,
    )

    assert figure_factory.figure.value.layout.xaxis.showline is True
    assert figure_factory.figure.value.layout.yaxis.showline is True

    assert figure_factory.figure.value.layout.xaxis.linewidth == 11
    assert figure_factory.figure.value.layout.yaxis.linewidth == 11

    assert figure_factory.figure.value.layout.xaxis.linecolor == "green"
    assert figure_factory.figure.value.layout.yaxis.linecolor == "green"


def test_set_zero_lines_dark(figure_factory):
    figure_factory.background_color = BackgroundColor.dark

    figure_factory.set_zero_lines(
        line_width=11, show_x_axis_zeroline=True, show_y_axis_zeroline=True
    )

    assert figure_factory.figure.value.layout.xaxis.showline is True
    assert figure_factory.figure.value.layout.yaxis.showline is True

    assert figure_factory.figure.value.layout.xaxis.linewidth == 11
    assert figure_factory.figure.value.layout.yaxis.linewidth == 11

    assert figure_factory.figure.value.layout.xaxis.linecolor == "white"
    assert figure_factory.figure.value.layout.yaxis.linecolor == "white"


def test_set_zero_lines_light(figure_factory):
    figure_factory.background_color = BackgroundColor.light

    figure_factory.set_zero_lines(
        line_width=11, show_x_axis_zeroline=True, show_y_axis_zeroline=True
    )

    assert figure_factory.figure.value.layout.xaxis.showline is True
    assert figure_factory.figure.value.layout.yaxis.showline is True

    assert figure_factory.figure.value.layout.xaxis.linewidth == 11
    assert figure_factory.figure.value.layout.yaxis.linewidth == 11

    assert figure_factory.figure.value.layout.xaxis.linecolor == "black"
    assert figure_factory.figure.value.layout.yaxis.linecolor == "black"


def test_set_xaxis_rotation(figure_factory):
    figure_factory.set_xaxis_rotation(degree=33)

    assert figure_factory.figure.value.layout.xaxis.tickangle == 33


def test_set_axis_label_color(figure_factory):
    figure_factory.set_axis_label_color(
        x_axis_label_color="green", y_axis_label_color="yellow"
    )

    assert figure_factory.figure.value.layout.xaxis.color == "green"
    assert figure_factory.figure.value.layout.yaxis.color == "yellow"


def test_set_axis_name_color(figure_factory):
    figure_factory.set_axis_name_color(x_axis_color="purple", y_axis_color="brown")

    assert figure_factory.figure.value.layout.xaxis.title.font.color == "purple"
    assert figure_factory.figure.value.layout.yaxis.title.font.color == "brown"


def test_set_axis_zeroline_color(figure_factory):
    figure_factory.set_axis_zeroline_color(
        x_zeroline_color="red", y_zeroline_color="blue"
    )

    assert figure_factory.figure.value.layout.xaxis.zerolinecolor == "red"
    assert figure_factory.figure.value.layout.yaxis.zerolinecolor == "blue"


def test_set_logarithmic_scale(figure_factory):
    figure_factory.set_logarithmic_scale(y_axis=True, x_axis=True)

    assert figure_factory.figure.value.layout.xaxis.type == "log"
    assert figure_factory.figure.value.layout.yaxis.type == "log"


def test_set_legend_position_top(figure_factory):
    figure_factory.set_legend_position(position=LegendPosition.TOP)

    assert figure_factory.figure.value.layout.legend.orientation == "v"
    assert figure_factory.figure.value.layout.legend.yanchor == "top"
    assert figure_factory.figure.value.layout.legend.xanchor == "right"
    assert figure_factory.figure.value.layout.legend.bgcolor == "rgba(255, 255, 255, 0)"


def test_set_legend_position_bottom(figure_factory):
    figure_factory.set_legend_position(position=LegendPosition.BOTTOM)

    assert figure_factory.figure.value.layout.legend.orientation == "h"
    assert figure_factory.figure.value.layout.legend.yanchor == "bottom"
    assert figure_factory.figure.value.layout.legend.bgcolor == "rgba(255, 255, 255, 0)"


def test_set_font_style(figure_factory):
    figure_factory.set_font_style(font_type="font_type_1", font_size=99)

    assert figure_factory.figure.value.layout.font.family == "font_type_1"
    assert figure_factory.figure.value.layout.font.size == 99

    assert figure_factory.figure.value.layout.hoverlabel.font.family == "font_type_1"
    assert figure_factory.figure.value.layout.hoverlabel.font.size == 99

    assert figure_factory.figure.value.layout.legend.font.family == "font_type_1"
    assert figure_factory.figure.value.layout.legend.font.size == 99

    assert figure_factory.figure.value.layout.xaxis.title.font.family == "font_type_1"
    assert figure_factory.figure.value.layout.xaxis.title.font.size == 99

    assert figure_factory.figure.value.layout.xaxis.tickfont.family == "font_type_1"

    assert figure_factory.figure.value.layout.yaxis.title.font.family == "font_type_1"
    assert figure_factory.figure.value.layout.yaxis.title.font.size == 99

    assert figure_factory.figure.value.layout.yaxis.tickfont.family == "font_type_1"


def test_set_yaxis_spacing(figure_factory):
    figure_factory.set_yaxis_spacing(number_of_spaces=2)

    assert figure_factory.figure.value.layout.yaxis.ticksuffix == 2 * " "


def test_set_yaxis_value_style_thousands(figure_factory):
    figure_factory.set_yaxis_value_style(style=ValueStyle.THOUSANDS)

    assert figure_factory.figure.value.layout.yaxis.tickformat == ",.0f"


def test_set_yaxis_value_style_k_notation(figure_factory):
    figure_factory.set_yaxis_value_style(style=ValueStyle.K_NOTATION)

    assert figure_factory.figure.value.layout.yaxis.tickformat == "~s"
