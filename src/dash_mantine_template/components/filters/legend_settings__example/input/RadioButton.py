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
def input__radio_button__legend_location() -> Input:
    """
    1
    """

    return gc.legend_settings.input_(id_=ID.legend_settings + "__legend_location")
