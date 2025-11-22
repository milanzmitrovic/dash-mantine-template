"""
Here we define all OUTPUT elements
of callback for legend_position__example
component.

These components will be used in
CallbackSignature.py files.

Here we instantiate components that
are defining attributes which are
updated via callback.
"""

from dash_mantine_template import gc

from ..ComponentID import ID


def output__data__legend_orientation():
    """
    1
    """
    return gc.legend_settings.output(
        id_=ID.legend_settings + "__legend_orientation", property_="data"
    )
