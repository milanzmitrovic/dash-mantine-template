"""
Purpose of this file is to hold multiselect
UI component.
"""

from typing import Optional

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, validate_call

from .Types import Radius, Size


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component(
    id_: Optional[str] = None,
    children: Optional[str] = None,
    size: Optional[Size] = None,
    radius: Optional[Radius] = None,
    loading: Optional[bool] = None,
    disabled: Optional[bool] = None,
):
    """
    UI function returning multiselect
    component.
    """

    # Dynamically add ID if provided.
    # Otherwise, do not provide ID in
    # case it is None.
    if id_ is not None:
        dict__id = {"id": id_}
    else:
        dict__id = {}

    return html.Div(
        children=[
            html.Div(id=id_ + "_dummy-input", n_clicks=77),
            dmc.Button(
                **dict__id,
                children=children,
                size=size,
                radius=radius,
                loading=loading,
                disabled=disabled,
            ),
        ]
    )
