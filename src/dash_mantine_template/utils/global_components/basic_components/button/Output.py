
"""
Purpose of this file is to hold function
that will help in organization of callback
OUTPUT related with button component.

Here we define what (default) property of
button component will be updated with
callback function.

<<<
button component is used as
OUTPUT of callback
<<<
<<<

Also, we wll be able to see what are all
places in which button was used
as OUTPUT in callback.
"""
from dash import Output
from pydantic import validate_call, ConfigDict


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def output(id_: str, property_: str = 'children') -> Output:
    """
    Purpose of this function is to help with
    creation of callback signature.
    """

    return Output(component_id=id_, component_property=property_)
