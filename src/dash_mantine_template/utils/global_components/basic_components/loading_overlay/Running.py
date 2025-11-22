"""
Purpose of this file is to help with organization
of callback signature that will be used ar running()
attribute in callback.
"""

from typing import Optional

from dash import Output


def running_(id_: str, property_: Optional[str] = "visible"):
    """
    Purpose of this function is to help with creation of
    callback signature that will be used as running()
    attribute in callback.
    """
    return (
        Output(component_id=id_ + "__loading-overlay", component_property=property_),
        True,
        False,
    )
