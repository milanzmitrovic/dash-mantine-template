"""
Here we define all OUTPUT elements
of callback for radio_button__example
component.

These components will be used in
CallbackSignature.py files.

Here we instantiate components that
are defining attributes which are
updated via callback.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def output__children():
    """
    1
    """
    return gc.radio_button.output(id_=ID.legend_position)


def output__value():
    """
    1
    """
    return gc.radio_button.output(id_=ID.legend_position, property_="value")
