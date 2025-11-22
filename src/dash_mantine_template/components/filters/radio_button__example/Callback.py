"""
1
"""

from dash import callback, html, no_update
from .CallbackSignature import inputs__all, output__all
import dash_mantine_components as dmc
from time import sleep
from pydantic import validate_call, ConfigDict
from .Types import RadioButtonOutput


@callback(
    inputs=inputs__all(),
    output=output__all(),
    hidden=True
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> RadioButtonOutput:
    """
    Purpose of this callback is to set
    initial values to radio_button component.

    It should be used to query relevant
    data from database and set up component
    with up-to-date values.
    """

    data = {
        'Top Left': 'top-left',
        'Top Right': 'top-right',
        'Bottom Left': 'bottom-left',
        'Bottom Right': 'bottom-right'
    }

    radio_elements = dmc.SimpleGrid([dmc.Radio(k, value=v) for k, v in data.items()], my=10, cols=2, w=300)

    sleep(3)

    return {
        'value': 'top-left',
        "children": radio_elements,
    }
