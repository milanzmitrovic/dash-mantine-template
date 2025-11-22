
"""
1
"""

from dash_mantine_template import gc
from .ComponentID import ID
from pydantic import validate_call, ConfigDict
import dash_mantine_components as dmc


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component() -> dmc.NumberInput:
    """
    1
    """

    return gc.number_input.component(
        id_=ID.number_input,
        label='Number Input Component',
        width=150
    )
