"""
Purpose of this file is to hold component
that will help in organization of input/state
related with pagination component.

Here we define what (default) property of
pagination component will trigger callback.

<<<
pagination component is used as
INPUT of callback
<<<

Also, we will be able to see what are all
places in which pagination was used
as INPUT in callback.
"""

from dash import Input, State
from pydantic import ConfigDict, validate_call

from .. import dummy_input


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def input_(
    id_: str, state: bool = False, property_: str = "value"
) -> State | Input | None:
    """
    Purpose of this function is to help with
    creation of callback signature.

    Default property is 'value' which represents the current page number.
    """

    if state:
        return State(component_id=id_, component_property=property_)

    elif not state:
        return Input(component_id=id_, component_property=property_)

    else:
        return None


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def input_dummy(id_: str) -> Input:
    """
    Purpose of this function is to create callback
    signature template for dummy input component.

    Dummy input component will be used to trigger initial
    load of component values.

    We need to load component's initial property
    values (that are dynamic in a sense that
    total number of pages can be altered based on
    data size and items per page).
    """

    return dummy_input.dummy_input(id_=id_)
