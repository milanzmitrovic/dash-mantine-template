"""
Purpose of this file is to help with
organization of dummy_component.
"""

from dash import html
from pydantic import ConfigDict, validate_call


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(id_: str):
    """
    Purpose of this function is to create
    component that will be used to hold
    dummy button.

    Dummy button will be used to initially
    trigger callback on page load.

    That callback should enrich component
    with data directly from database.
    """

    # n_clicks must have any number. Why?
    # Otherwise, it will have value of None
    # which will cause Pydantic error when
    # validating callback input.
    return html.Div(id=id_ + "_dummy-input", n_clicks=77)
