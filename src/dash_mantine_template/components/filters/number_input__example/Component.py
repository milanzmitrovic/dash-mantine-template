"""
Purpose of this file is to define UI
component that will be used in app.
"""

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call

from dash_mantine_template import gc

from .ComponentID import ID


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component() -> dmc.NumberInput:
    """
    1
    """

    return gc.number_input.component(
        id_=ID.number_input, label="Number Input Component", width=150
    )
