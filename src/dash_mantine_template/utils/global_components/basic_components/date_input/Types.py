"""
Purpose of this file is to define types
used in date_input component.
"""

from typing import TypedDict


class DateInputDict(TypedDict):
    """
    This type is not commonly used for date input,
    but included for consistency with other components.
    """

    value: str
    label: str
