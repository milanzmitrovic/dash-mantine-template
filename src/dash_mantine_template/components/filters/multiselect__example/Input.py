"""
Here we define all INPUT elements
of callback for multiselect__example
component.

These components will be used in
CallbackSignature.py files.

All components that depend on
multiselect__example component (i.e.
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
    return gc.multiselect.input_dummy(id_=ID.multiselect)


def input_():
    """
    1
    """
    return gc.multiselect.input_(id_=ID.multiselect)
