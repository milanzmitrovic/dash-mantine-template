"""
1
"""

from dash import callback
from .CallbackSignature import inputs__all, output__all
from pydantic import validate_call, ConfigDict


@callback(
    inputs=inputs__all(),
    output=output__all(),
    # hidden=True
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int):
    """
    Purpose of this callback is to set
    initial values to button component.

    It should be used to query relevant
    data from database and set up component
    with up-to-date values.
    """

    button_text = 'test test'

    return {
        "children": button_text,
    }
