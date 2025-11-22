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
    return gc.select.input_dummy(id_=ID.select)
