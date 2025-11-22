"""
This file is holding logic that defines
return type of callback function.
"""

from typing import List, TypedDict


class OutputItem(TypedDict):
    """
    1
    """

    value: str
    label: str


class Output(TypedDict):
    """
    1
    """

    data: List[OutputItem]
    # value: NoUpdate
