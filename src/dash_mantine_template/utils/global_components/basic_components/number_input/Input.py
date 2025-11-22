
"""
Purpose of this file is to hold component
that will help in organization of input/state
related with number_input component.

Here we define what (default) property of
number_input component will trigger callback.

<<<
number_input component is used as
INPUT of callback
<<<
<<<

Also, we wll be able to see what are all
places in which number_input was used
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
