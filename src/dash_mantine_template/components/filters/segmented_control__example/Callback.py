"""
1
"""

from dash import callback, html, no_update
from .CallbackSignature import inputs__all, output__all
import dash_mantine_components as dmc
from time import sleep
from .Types import SegmentedControlOutput
from pydantic import validate_call, ConfigDict


@callback(
    inputs=inputs__all(),
    output=output__all(),
    hidden=True
)
# @validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> SegmentedControlOutput:
    """
    Purpose of this callback is to set
    initial values to segmented_control component.

    It should be used to query relevant
    data from database and set up component
    with up-to-date values.
    """

    data = ['Serbia', 'UK', 'Germany', 'France']

    value = 'France'

    sleep(3)

    return {
        "data": data,
        "value": value,
    }
