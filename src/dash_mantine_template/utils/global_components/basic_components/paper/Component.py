"""
Purpose of this file is to hold paper()
UI component.
"""

from typing import List, Optional

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(
    id_: Optional[str] = None,
    children: Optional[List] = None,
    radius: Optional[str] = None,
    padding: Optional[str] = None,
    shadow: Optional[str] = None,
    with_border: Optional[bool] = None,
):
    """
    Purpose of this function is to create
    dmc.Paper() component.
    """

    # Dynamically add ID if provided.
    # Otherwise, do not provide ID in
    # case it is None.
    if id_ is not None:
        dict__id = {"id": id_}
    else:
        dict__id = {}

    return dmc.Paper(
        **dict__id,
        children=children,
        radius=radius,
        p=padding,
        shadow=shadow,
        withBorder=with_border,
    )
