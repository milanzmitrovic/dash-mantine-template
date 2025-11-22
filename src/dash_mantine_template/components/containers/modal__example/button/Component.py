"""
Purpose of this file is to define UI
component that will be used in app.
"""

from dash import html
from pydantic import ConfigDict, validate_call

from dash_mantine_template import gc

from .ComponentID import ID


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component() -> html.Div:
    """
    Purpose of this function is to instantiate
    UI component that will be used in application.

    ID and other parameters are provided in this
    step.

    This button controls modal__example.
    When clicked, it opens the modal.
    """

    return gc.button.component(id_=ID.button, children="Open Modal")
