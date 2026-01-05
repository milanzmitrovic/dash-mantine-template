"""
Purpose of this file is to hold date input
UI component.
"""

from datetime import date
from typing import Optional

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, StrictInt, validate_call

from .. import dummy_input


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(
    id_: str,
    value: Optional[str | date] = None,
    label: Optional[str] = None,
    placeholder: Optional[str] = None,
    description: Optional[str] = None,
    min_date: Optional[str | date] = None,
    max_date: Optional[str | date] = None,
    value_format: Optional[str] = "YYYY-MM-DD",
    width: Optional[StrictInt] = None,
    clearable: Optional[bool] = True,
    disabled: Optional[bool] = False,
):
    """
    UI function returning date input
    component.

    Parameters:
    - id_: Component identifier
    - value: Selected date (can be string in YYYY-MM-DD format or date object)
    - label: Label displayed above the input
    - placeholder: Placeholder text when no date is selected
    - description: Description text below the input
    - minDate: Minimum selectable date
    - maxDate: Maximum selectable date
    - valueFormat: Format for displaying the date (default: "YYYY-MM-DD")
    - width: Component width in pixels
    - clearable: Whether the input can be cleared
    - disabled: Whether the input is disabled
    """

    return html.Div(
        [
            # This component will be used to trigger
            # initial enrichment of component with
            # fresh data from database.
            dummy_input.component(id_=id_),
            dmc.DateInput(
                id=id_,
                value=value,
                label=label,
                placeholder=placeholder,
                description=description,
                minDate=min_date,
                maxDate=max_date,
                valueFormat=value_format,
                w=width,
                clearable=clearable,
                disabled=disabled,
            ),
        ]
    )
