"""
This file is used to define callback logic.

"""

from typing import List

from dash import callback
from pydantic import ConfigDict, validate_call

from ..callback_signature.SegmentedControl import inputs__all, output__all
from ..types import SegmentedControl


@callback(inputs=inputs__all(), output=output__all(), hidden=True)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> SegmentedControl.Output:
    """
    Purpose of this callback is to set
    initial values to data attribute
    of segmented_control component inside its
    parent legend_settings component.

    Property 'value' should not be updated
    because it will re-trigger chart rendering.

    It should be used to query relevant
    data from database and set up component
    with up-to-date values.
    """

    data: List[SegmentedControl.OutputItem] = [
        {"value": "horizontal", "label": "Horizontal"},
        {"value": "vertical", "label": "Vertical"},
    ]

    return {
        "data": data,
        # "value": dash.no_update,
    }
