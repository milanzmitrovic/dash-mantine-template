"""
This file is used to define callback logic.

"""

import dash
import dash_mantine_components as dmc
from dash import callback
from pydantic import ConfigDict, validate_call

from ..callback_signature.RadioButton import inputs__all, output__all
from ..types import RadioButton


@callback(inputs=inputs__all(), output=output__all(), hidden=True)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> RadioButton.Output:
    """
    Purpose of this callback is to set
    INITIAL values to children attribute
    of radio_button component inside its
    parent legend_settings component.

    Property 'value' should not be updated
    because it will re-trigger chart rendering.

    It should be used to query relevant
    data from database and set up component
    with up-to-date values.
    """

    data = {
        "Top Left": "top-left",
        "Top Right": "top-right",
        "Bottom Left": "bottom-left",
        "Bottom Right": "bottom-right",
    }

    radio_elements = dmc.SimpleGrid(
        [dmc.Radio(k, value=v) for k, v in data.items()], my=10, cols=2, w=300
    )

    return {"children": radio_elements, "value": dash.no_update}
