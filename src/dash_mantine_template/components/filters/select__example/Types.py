"""
This file is holding logic that defines
return type of callback function.
"""

from typing import List, TypedDict

import dash


class SelectOutput(TypedDict):
    """
    Purpose of this class is to define type of
    output that will be returned in callback function.
    """

    data: List[str]
    value: str | dash.NoUpdate
