"""
Purpose of this file is to define types
used in modal component.
"""

from typing import TypedDict


class ModalDict(TypedDict):
    """
    This type is not commonly used for modal,
    but included for consistency with other components.
    """

    value: str
    label: str
