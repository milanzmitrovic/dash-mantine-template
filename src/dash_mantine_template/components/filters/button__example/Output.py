"""
Here we define all OUTPUT elements
of callback for button__example
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
    return gc.button.output(id_=ID.button)
