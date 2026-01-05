"""
Purpose of this file is to hold function
that will help in organization of callback
OUTPUT related with pagination component.

Here we define what (default) property of
pagination component will be updated with
callback function.

<<<
pagination component is used as
OUTPUT of callback
<<<

Also, we will be able to see what are all
places in which pagination was used
as OUTPUT in callback.
"""

from dash import Output
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def output(id_: str, property_: str = "total") -> Output:
    """
    Purpose of this function is to help with
    creation of callback signature.

    Default property is 'total' which represents the total number of pages.
    This is typically what you'd update when data changes.
    """

    return Output(component_id=id_, component_property=property_)
