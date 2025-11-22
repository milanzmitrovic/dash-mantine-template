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


def output__value__pixel_x():
    """
    1
    """
    return gc.legend_settings.output(
        id_=ID.legend_settings + "__position_x", property_="value"
    )


def output__value__pixel_y():
    """
    1
    """
    return gc.legend_settings.output(
        id_=ID.legend_settings + "__position_y", property_="value"
    )
