
"""
Purpose of this file is to hold component
that will help in organization of input/state
related with radio_button component.

Here we define what (default) property of
radio_button component will trigger callback.

<<<
radio_button component is used as
INPUT of callback
<<<
<<<

Also, we wll be able to see what are all
places in which radio_button was used
as INPUT in callback.
"""
from dash import Input, State
from pydantic import validate_call, ConfigDict


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def input_(id_: str, state: bool = False, property_: str = 'value') -> State | Input | None:
    """
    Purpose of this function is to help with
    creation of callback signature.
    """

    if state:

        return State(component_id=id_, component_property=property_)

    elif not state:
        return Input(component_id=id_, component_property=property_)

    else:
        return None


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def input_dummy(id_: str) -> Input:
    """
    Purpose of this function is to create dummy
    input component.

    This component will be used to trigger initial
    load of component values.

    We need to load component's initial property
    values (that are dynamic in a sense that
    potential values of component can be altered i.e.
    added or removed).
    """

    return Input(component_id=id_ + '_dummy-input', component_property='n_clicks')
