"""
Purpose of this file is to hold multiselect
UI component.
"""

import dash_mantine_components as dmc
from dash import html
from typing import Optional
from .Types import Size, Radius
from pydantic import validate_call, ConfigDict


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component(
        id_: str,
        children: Optional[str] = None,
        size: Optional[Size] = None,
        radius: Optional[Radius] = None,
        loading: Optional[bool] = None,
        disabled: Optional[bool] = None
):
    """
    UI function returning multiselect
    component.
    """

    return html.Div(
        children=[
            html.Div(id=id_ + "_dummy-input", n_clicks=77),
            dmc.Button(
                id=id_,
                children=children,
                size=size,
                radius=radius,
                loading=loading,
                disabled=disabled
            ),
        ]
    )
