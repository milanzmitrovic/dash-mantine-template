"""
1
"""

from dash_mantine_template import gc
from .ComponentID import ID
from .Callback import *
import dash_mantine_components as dmc


def component():
    """
    1
    """

    return dmc.Container(children=[
        gc.multiselect.component(
        id_=ID.multiselect,
        value=[],
        data=[],
        label='Multiselect Component'
    )], w=500
    )
