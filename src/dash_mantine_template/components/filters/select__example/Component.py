"""
1
"""

from dash_mantine_template import gc
from .ComponentID import ID
from .Callback import *
import dash_mantine_components as dmc
from pydantic import validate_call, ConfigDict


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component() -> dmc.Container:
    """
    1
    """

    return dmc.Container(children=[
        gc.select.component(
        id_=ID.select,
        value='',
        data=[],
        label='Select Component'
    )], w=500
    )
