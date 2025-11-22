"""
This file is holding logic that defines
return type of callback function.
"""

from typing import TypedDict

import dash_mantine_components as dmc


class RadioButtonOutput(TypedDict):
    """
    1
    """

    children: dmc.SimpleGrid
    value: str
