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


def output__data():
    """
    1
    """
    return gc.multiselect.output(id_=ID.multiselect)


def output__value():
    """
    1
    """
    return gc.multiselect.output(id_=ID.multiselect, property_="value")
