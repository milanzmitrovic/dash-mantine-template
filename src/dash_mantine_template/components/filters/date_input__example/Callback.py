"""
This file is used to define callback logic.
"""

from datetime import date, timedelta
from time import sleep

from dash import callback
from pydantic import ConfigDict, validate_call

from .CallbackSignature import inputs__all, output__all, running__all
from .Types import DateInputOutput


@callback(
    inputs=inputs__all(), output=output__all(), running=running__all(), hidden=True
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> DateInputOutput:
    """
    Purpose of this callback is to set
    initial values to date_input component.

    It should be used to query relevant
    data from database and set up component
    with appropriate:
    - Default date value
    - Minimum selectable date
    - Maximum selectable date

    Example use cases:
    - Set default to today's date
    - Restrict date range based on business rules
    - Set date based on user's last activity
    """

    # Example: Set default to today
    today = date.today()

    # Example: Allow dates from 30 days ago to 30 days in future
    min_date = today - timedelta(days=30)
    max_date = today + timedelta(days=30)

    # Alternative: Query from database
    # default_date = query_user_last_activity_date()
    # min_date = query_contract_start_date()
    # max_date = query_contract_end_date()

    sleep(3)

    return {
        # Set default value
        "value": today.strftime("%Y-%m-%d"),
        # Set date range constraints
        "minDate": min_date.strftime("%Y-%m-%d"),
        "maxDate": max_date.strftime("%Y-%m-%d"),
        # If you don't want to update these properties initially:
        # "value": dash.no_update,
        # "minDate": dash.no_update,
        # "maxDate": dash.no_update,
    }
