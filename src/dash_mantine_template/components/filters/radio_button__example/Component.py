"""
Purpose of this file is to define UI
component that will be used in app.
"""

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, validate_call

from dash_mantine_template import gc

from .Callback import *  # noqa: F403
from .ComponentID import ID


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component() -> dmc.Container:
    """
    1
    """

    return dmc.Container(
        children=[
            gc.radio_button.component(
                id_=ID.legend_position,
                children=html.Div(),
                value="",
                label="Radio Button Component",
            )
        ],
        w=500,
    )
