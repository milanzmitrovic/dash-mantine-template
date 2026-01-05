"""
This file is used to define callback logic.

"""

import dash
from dash import callback
from pydantic import ConfigDict, validate_call

from ..callback_signature.PositionXY import inputs__all, output__all
from ..types import PositionXY


@callback(
    inputs=inputs__all(),
    output=output__all(),
    hidden=True,
    config_prevent_initial_callbacks=True,
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(legend_location: str) -> PositionXY.Output:
    """
    Purpose of this callback is to set
    values to following components:
        Position X
        Position Y

    When user chooses location of legend
    (Top Left, Bottom Right, ...) then
    value of location input components
    should be updated accordingly.

    Legend is controlled by position_x and
    position_y input fields. They are used
    as inputs in callback that is returning
    Plotly chart.

    """

    if legend_location == "top-left":
        pixel_x = 1
        pixel_y = 1

    elif legend_location == "top-right":
        pixel_x = 2
        pixel_y = 2

    elif legend_location == "bottom-left":
        pixel_x = 3
        pixel_y = 3

    elif legend_location == "bottom-right":
        pixel_x = 4
        pixel_y = 4

    else:
        pixel_x = dash.no_update
        pixel_y = dash.no_update

    return {
        "pixel_x": pixel_x,
        "pixel_y": pixel_y,
    }
