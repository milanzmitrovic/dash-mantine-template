"""
Purpose of this file is to hold function
that will help in organization of callback
OUTPUT related with modal component.

Here we define what (default) property of
modal component will be updated with
callback function.

<<<
modal component is used as
OUTPUT of callback
<<<

Also, we will be able to see what are all
places in which modal was used
as OUTPUT in callback.
"""

from dash import Output
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def output(id_: str, property_: str = "opened") -> Output:
    """
    Purpose of this function is to help with
    creation of callback signature.

    Default property is 'opened' which controls whether modal is visible.
    This is typically what external buttons will update.
    """

    return Output(component_id=id_, component_property=property_)
