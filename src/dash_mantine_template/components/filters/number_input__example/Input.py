"""
Here we define all INPUT elements
of callback for number_input_example
component.

These components will be used in
CallbackSignature.py files.

All components that depend on
number_input_example component (i.e.
have it as input/state dependency)
will use these functions in their
CallbackSignature.py file.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def input_():
    """
    1
    """
    return gc.number_input.input_(id_=ID.number_input)
