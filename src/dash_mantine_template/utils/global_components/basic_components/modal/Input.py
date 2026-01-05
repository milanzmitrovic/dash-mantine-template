"""
Purpose of this file is to hold component
that will help in organization of input/state
related with modal component.

Here we define what (default) property of
modal component will trigger callback.

<<<
modal component is used as
INPUT of callback
<<<

Also, we will be able to see what are all
places in which modal was used
as INPUT in callback.
"""

from dash import Input, State
from pydantic import ConfigDict, validate_call


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def input_(
    id_: str, state: bool = False, property_: str = "opened"
) -> State | Input | None:
    """
    Purpose of this function is to help with
    creation of callback signature.

    Default property is 'opened' which represents whether modal is open.
    This can be used to trigger callbacks when modal opens/closes.
    """

    if state:
        return State(component_id=id_, component_property=property_)

    elif not state:
        return Input(component_id=id_, component_property=property_)

    else:
        return None
