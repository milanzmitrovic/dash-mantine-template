"""
Here we define all OUTPUT elements
of callback for select_example
component.

These components will be used in
CallbackSignature.py files.

Here we instantiate components that
are defining attributes which are
updated via callback.

"""

from dash_mantine_template import gc

from .ComponentID import ID


def output__data():
    """
    Here we instantiate <data> property of
    component that is being updated via callback.
    """
    return gc.multiselect.output(id_=ID.select)


def output__value():
    """
    Here we instantiate <value> property of
    component that is being updated via callback.
    """
    return gc.select.output(id_=ID.select, property_="value")
