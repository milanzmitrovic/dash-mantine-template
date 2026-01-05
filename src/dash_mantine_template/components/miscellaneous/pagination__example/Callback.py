"""
This file is used to define callback logic.
"""

import math
from time import sleep

import dash
from dash import callback
from pydantic import ConfigDict, validate_call

from .CallbackSignature import inputs__all, output__all, running__all
from .Types import PaginationOutput


@callback(
    inputs=inputs__all(), output=output__all(), running=running__all(), hidden=True
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> PaginationOutput:
    """
    Purpose of this callback is to set
    initial values to pagination component.

    It should be used to query relevant
    data from database and calculate total
    number of pages based on:
    - Total number of items in database
    - Items per page

    Example calculation:
    total_items = 145
    items_per_page = 10
    total_pages = math.ceil(145 / 10) = 15
    """

    # Example: Query database to get total number of items
    # total_items = query_database_count()
    total_items = 145

    # Define items per page
    items_per_page = 10

    # Calculate total pages
    total_pages = math.ceil(total_items / items_per_page)

    sleep(1)

    return {
        "total": total_pages,
        # If "value" is returned here instead of
        # dash.no_update, then unnecessary
        # recalculation of callback could be triggered.
        # But, if pagination component is used as STATE type
        # instead of INPUT, then this can be avoided.
        "value": dash.no_update,
    }
