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
        gc.button.component(
        id_=ID.button,
    )], w=500
    )
