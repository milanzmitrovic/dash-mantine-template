"""
Here we define all INPUT elements
of callback for radio_button__legend_position
component.
"""


from dash_mantine_template import gc
from .ComponentID import ID


def input_dummy():
    """
    1
    """
    return gc.segmented_control.input_dummy(id_=ID.segmented_control)
