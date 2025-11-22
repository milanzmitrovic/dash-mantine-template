"""
Purpose of this file is to define UI
component that will be used in app.
"""

import dash_mantine_components as dmc

from dash_mantine_template import gc

from .Callback import *  # noqa: F403
from .ComponentID import ID


def component():
    """
    1
    """

    return dmc.Container(
        children=[
            gc.loading_overlay.component(
                id_=ID.multiselect,
                children=[
                    gc.multiselect.component(
                        id_=ID.multiselect,
                        value=[],
                        data=[],
                        label="Multiselect Component",
                    )
                ],
            )
        ],
        w=500,
    )
