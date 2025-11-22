"""
This file is holding logic that defines
return type of callback function.
"""

from typing import TypedDict

import dash


class PaginationOutput(TypedDict):
    """
    Purpose of this class is to define type of
    output that will be returned in callback function.
    """

    total: int
    value: int | dash.NoUpdate
