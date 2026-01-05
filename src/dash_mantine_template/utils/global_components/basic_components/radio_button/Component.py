"""
Purpose of this file is to hold number_input
UI component.
"""

from typing import Optional

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, validate_call

from .Types import Size


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component(
    id_: str,
    children: html.Div,
    value: Optional[str] = None,
    label: Optional[str] = None,
    size: Optional[Size] = None,
) -> html.Div:
    """
    UI function returning radio_button
    component.
    """

    return html.Div(
        children=[
            html.Div(id=id_ + "_dummy-input", n_clicks=77),
            dmc.RadioGroup(
                id=id_,
                children=children,
                value=value,
                label=label,
                size=size,
            ),
        ]
    )
