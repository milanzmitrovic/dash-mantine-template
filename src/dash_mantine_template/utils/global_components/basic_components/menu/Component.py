"""
Purpose of this file is to facilitate logic
for creation of dmc.Menu() component.
"""

from typing import List, Optional

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call

from .Types import Trigger


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(
    children: List, id_: Optional[str] = None, trigger: Optional[Trigger] = None
):
    """
    Purpose of this function is to create
    UI element that will represent dmc.Menu()
    component.
    """

    # Dynamically add ID if provided.
    # Otherwise, do not provide ID in
    # case it is None.
    if id_ is not None:
        dict__id = {"id": id_}
    else:
        dict__id = {}

    return dmc.Menu(**dict__id, children=children, trigger=trigger)
