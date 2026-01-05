"""
This file is holding logic that defines
return type of callback function.
"""

from typing import TypedDict

import dash


class ModalOutput(TypedDict):
    """
    Purpose of this class is to define type of
    output that will be returned in callback function.

    Note: Modal's initial callback typically doesn't
    need to return anything, as it's controlled externally.
    This is here for consistency with the pattern.
    """

    opened: bool | dash.NoUpdate
