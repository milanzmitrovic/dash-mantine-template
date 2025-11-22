"""
Purpose of this file is to hold simple_grid
UI component.
"""

from typing import List, Optional

import dash_mantine_components as dmc
from pydantic import ConfigDict, StrictInt, validate_call


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(
    number_of_columns: StrictInt,
    id_: Optional[str] = None,
    children: Optional[List] = None,
    spacing: Optional[str] = None,
    vertical_spacing: Optional[str] = None,
):
    """
    Purpose of this function is to create component
    that will hold all other components in dmc.SimpleGrid().
    """

    # Dynamically add ID if provided.
    # Otherwise, do not provide ID in
    # case it is None.
    if id_ is not None:
        dict__id = {"id": id_}
    else:
        dict__id = {}

    return dmc.SimpleGrid(
        **dict__id,
        children=children,
        cols=number_of_columns,
        spacing=spacing,
        verticalSpacing=vertical_spacing,
    )
