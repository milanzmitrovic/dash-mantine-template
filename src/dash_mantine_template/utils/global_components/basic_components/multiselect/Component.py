"""
Purpose of this file is to hold multiselect
UI component.
"""

from typing import List, Optional

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, validate_call

from .Types import DataDict


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(
    id_: str,
    value: List[str],
    data: DataDict | List,
    label: Optional[str] = None,
    placeholder: Optional[str] = None,
    width: Optional[int] = None,
):
    """
    UI function returning multiselect
    component.
    """

    return html.Div(
        children=[
            html.Div(id=id_ + "_dummy-input", n_clicks=77),
            dmc.MultiSelect(
                id=id_,
                value=value,
                label=label,
                placeholder=placeholder,
                data=data,
                w=width,
            ),
        ]
    )
