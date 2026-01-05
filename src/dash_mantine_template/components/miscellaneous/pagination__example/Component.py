"""
Purpose of this file is to define UI
component that will be used in app.
"""

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call

from dash_mantine_template import gc

from .Callback import *  #  noqa: F403
from .ComponentID import ID  # ruff: noqa: F401


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component() -> dmc.Container:
    """
    Purpose of this function is to instantiate
    UI component that will be used in application.

    ID and other parameters are provided in this
    step.
    """

    return dmc.Container(
        children=[
            gc.loading_overlay.component(
                id_=ID.pagination,
                children=[
                    gc.pagination.component(
                        id_=ID.pagination,
                        value=1,
                        total=1,
                        siblings=1,
                        boundaries=1,
                        size="md",
                        radius="sm",
                    )
                ],
            )
        ],
        w=500,
    )
