"""
1
"""

from dash_mantine_template import gc
from .ComponentID import ID
from .Callback import *
from dash import html
import dash_mantine_components as dmc
from pydantic import validate_call, ConfigDict


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component() -> dmc.Container:
    """
    1
    """

    return dmc.Container(children=[
        gc.radio_button.component(
        id_=ID.legend_position,
        children=html.Div(),
        value='',
        label='Radio Button Component'
    )], w=500
    )
