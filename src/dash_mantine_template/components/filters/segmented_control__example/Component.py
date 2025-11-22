"""
1
"""

import dash_mantine_components as dmc
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
            gc.segmented_control.component(
                id_=ID.segmented_control,
                value="",
                data=[],
            )
        ],
        w=500,
    )
