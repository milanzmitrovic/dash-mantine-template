"""
Here we define all INPUT elements
of callback for legend_settings
component.
"""

from dash import Input
from pydantic import ConfigDict, validate_call

from dash_mantine_template import gc

from ..ComponentID import ID


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def input__position_x() -> Input:
    """
    1
    """

    return gc.legend_settings.input_(id_=ID.legend_settings + "__position_x")


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def input__position_y() -> Input:
    """
    1
    """

    return gc.legend_settings.input_(id_=ID.legend_settings + "__position_y")
