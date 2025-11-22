"""
1
"""

import dash_mantine_components as dmc
from pydantic import validate_call, ConfigDict
from typing import List, Optional
from .Types import Trigger


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component(children: List, trigger: Optional[Trigger] = None):
    """
    1
    """

    return dmc.Menu(children=children, trigger=trigger)
