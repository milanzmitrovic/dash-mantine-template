"""
Here we define all INPUT elements
of callback for radio_button__example
component.

These components will be used in
CallbackSignature.py files.

All components that depend on
radio_button__example component (i.e.
have it as input/state dependency)
will use these functions in their
CallbackSignature.py file.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def input_dummy():
    """
    1
    """
    return gc.radio_button.input_dummy(id_=ID.legend_position)


def input_():
    """
    1
    """
    return gc.radio_button.input_(id_=ID.legend_position)
