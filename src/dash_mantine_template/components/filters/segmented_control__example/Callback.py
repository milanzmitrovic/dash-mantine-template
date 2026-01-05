"""
1
"""

from time import sleep

from dash import callback
from pydantic import ConfigDict, validate_call

from .CallbackSignature import inputs__all, output__all
from .Types import SegmentedControlOutput


@callback(inputs=inputs__all(), output=output__all(), hidden=True)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> SegmentedControlOutput:
    """
    Purpose of this callback is to set
    initial values to segmented_control component.

    It should be used to query relevant
    data from database and set up component
    with up-to-date values.
    """

    data = ["Serbia", "UK", "Germany", "France"]

    value = "France"

    sleep(3)

    return {
        "data": data,
        "value": value,
    }
