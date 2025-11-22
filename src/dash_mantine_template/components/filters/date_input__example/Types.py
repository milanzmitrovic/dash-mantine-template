"""
This file is holding logic that defines
return type of callback function.
"""

from datetime import date
from typing import TypedDict

import dash


class DateInputOutput(TypedDict):
    """
    Purpose of this class is to define type of
    output that will be returned in callback function.
    """

    value: str | date | None | dash.NoUpdate
    minDate: str | date | None | dash.NoUpdate
    maxDate: str | date | None | dash.NoUpdate
    # loading_overlay: bool
