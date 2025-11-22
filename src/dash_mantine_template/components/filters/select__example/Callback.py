"""
This file is used to define callback logic.
"""

import dash
from dash import callback
from pydantic import ConfigDict, validate_call

from .CallbackSignature import inputs__all, output__all, running__all
from .Types import SelectOutput


@callback(
    inputs=inputs__all(), output=output__all(), running=running__all(), hidden=True
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def f(dummy_input: int) -> SelectOutput:
    """
    Purpose of this callback is to set
    initial values to select component.

    It should be used to query relevant
    data from database and set up component
    with up-to-date values.
    """

    data = ["Serbia", "UK", "Germany", "France"]

    return {
        "data": data,
        # If "value" is returned here instead of
        # dash.no_update, then unnecessary
        # recalculation of callback could be triggered.
        # But, if filter components are used as STATE type
        # instead of INPUT, then this can be avoided.
        # But, then question rises, who and how would
        # trigger apply-filters button?
        # Some logic should be developed...
        "value": dash.no_update,
    }
