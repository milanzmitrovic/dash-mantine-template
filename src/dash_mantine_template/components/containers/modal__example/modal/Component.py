"""
Purpose of this file is to define UI
component that will be used in app.
"""

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, validate_call

from dash_mantine_template import gc

from .Callback import *  # noqa: F403
from .ComponentID import ID


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component() -> html.Div:
    """
    Purpose of this function is to instantiate
    UI component that will be used in application.

    ID and other parameters are provided in this
    step.

    Note: Modal is controlled externally.
    See button__example for the control mechanism.
    """

    # return dmc.Button()

    return gc.modal.component(
        id_=ID.modal,
        title="Example Modal",
        size="lg",
        children=[
            dmc.Text("This is the modal content!", size="lg"),
            dmc.Space(h=20),
            dmc.Text("This modal is controlled by button__example component."),
            dmc.Space(h=20),
            dmc.Text("You can close it by:"),
            dmc.List(
                [
                    dmc.ListItem("Clicking the X button"),
                    dmc.ListItem("Pressing Escape key"),
                    dmc.ListItem("Clicking outside the modal"),
                ]
            ),
        ],
    )
