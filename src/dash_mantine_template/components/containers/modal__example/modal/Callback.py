"""
This file is used to define callback logic.
"""

from dash import callback
from pydantic import ConfigDict, validate_call

from .CallbackSignature import inputs__all, output__all
from .Types import ModalOutput


@callback(
    inputs=inputs__all(),
    output=output__all(),
    hidden=True,
    config_prevent_initial_callbacks=True,
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> ModalOutput:
    """
    Purpose of this callback is to set
    initial values to modal component.

    Since modal is controlled externally by buttons,
    this callback typically just ensures the modal
    starts in closed state.

    If you need to populate modal content from database,
    you would add additional outputs here for 'children'
    or other properties.
    """

    return {
        "opened": True,
    }
