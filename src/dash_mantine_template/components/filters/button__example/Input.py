"""
Here we define all INPUT elements
of callback for button_example
component.

These components will be used in
CallbackSignature.py files.

All components that depends on
select_example component (i.e.
have it as input/state dependency)
will use these functions its
CallbackSignature.py file.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def input_dummy():
    """
    1
    """
    return gc.button.input_dummy(id_=ID.button)


def input_():
    """
    1
    """
    return gc.button.input_(id_=ID.button)
