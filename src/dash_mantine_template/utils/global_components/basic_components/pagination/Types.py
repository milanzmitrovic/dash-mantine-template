"""
Purpose of this file is to define types
used in pagination component.
"""

from typing import TypedDict


class PaginationDict(TypedDict):
    """
    This type is not commonly used for pagination,
    but included for consistency with other components.
    """

    value: str
    label: str
