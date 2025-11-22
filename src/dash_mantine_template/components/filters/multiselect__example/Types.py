"""
This file is holding logic that defines
return type of callback function.
"""

from typing import List, TypedDict


class MultiselectOutput(TypedDict):
    """
    1
    """

    data: List[str]
    value: List[str]
