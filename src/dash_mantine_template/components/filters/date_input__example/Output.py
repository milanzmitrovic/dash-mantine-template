"""
Here we define all OUTPUT elements
of callback for date_input_example
component.

These components will be used in
CallbackSignature.py files.

Here we instantiate components that
are defining attributes which are
updated via callback.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def output__value():
    """
    Here we instantiate <value> property of
    component that is being updated via callback.

    This represents the selected date.
    """
    return gc.date_input.output(id_=ID.date_input, property_="value")


def output__minDate():
    """
    Here we instantiate <minDate> property of
    component that is being updated via callback.

    This sets the minimum selectable date.
    """
    return gc.date_input.output(id_=ID.date_input, property_="minDate")


def output__maxDate():
    """
    Here we instantiate <maxDate> property of
    component that is being updated via callback.

    This sets the maximum selectable date.
    """
    return gc.date_input.output(id_=ID.date_input, property_="maxDate")
