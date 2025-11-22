"""
Purpose of this file is to hold component
that will help in organization of input/state
related with legend_settings component.

Here we define what (default) property of
legend_settings component will trigger callback.

<<<
legend_settings component is used as
INPUT of callback
<<<
<<<

Also, we wll be able to see what are all
places in which legend_settings was used
as INPUT in callback.
"""

from dash import Input, State
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def input_(
    id_: str, state: bool = False, property_: str = "value"
) -> State | Input | None:
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

    return Input(component_id=id_ + "_dummy-input", component_property="n_clicks")
