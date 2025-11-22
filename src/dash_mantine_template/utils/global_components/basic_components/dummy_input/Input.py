"""
Purpose of this file is to hold component
that will help in organization of input/state
related with dummy_input component.

Here we define what (default) property of
dummy_input component will trigger callback.

<<<
dummy_input component is used as
INPUT of callback
<<<
<<<

Also, we wll be able to see what are all
places in which dummy_input was used
as INPUT in callback.
"""

from dash import Input


def dummy_input(id_: str):
    """
    Purpose of this function is to create
    callback signature for input_dummy component.
    """
    return Input(component_id=id_ + "_dummy-input", component_property="n_clicks")
