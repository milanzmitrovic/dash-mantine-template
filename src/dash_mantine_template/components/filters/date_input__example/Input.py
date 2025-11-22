"""
Here we define all INPUT elements
of callback for date_input_example
component.

These components will be used in
CallbackSignature.py files.

All components that depend on
date_input_example component (i.e.
have it as input/state dependency)
will use these functions in their
CallbackSignature.py file.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def input_dummy():
    """
    This will be typically used ONLY in callback
    that is setting initial values to UI component.

    Values are queried from database or set based
    on business logic.

    Component properties such as <value>, <minDate>,
    <maxDate> will be updated initially via callback.
    """
    return gc.date_input.input_dummy(id_=ID.date_input)


def input_():
    """
    This will be used in all components that
    depend on date_input_example component i.e.
    in all components that have date_input_example
    as input/state dependency.

    This typically triggers when user selects a date.
    """
    return gc.date_input.input_(id_=ID.date_input)
