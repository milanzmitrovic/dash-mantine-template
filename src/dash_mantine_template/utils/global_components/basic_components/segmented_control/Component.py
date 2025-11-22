"""
Purpose of this file is to hold multiselect
UI component.
"""

import dash_mantine_components as dmc
from dash import html
from typing import Optional, TypedDict, List
from .Types import DataDict
from pydantic import validate_call, ConfigDict


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component(
        id_: str,
        value: str,
        data: DataDict | List,
        width: Optional[int] = None
):
    """
    UI function returning multiselect
    component.
    """

    return html.Div(
        children=[
            html.Div(id=id_ + "_dummy-input", n_clicks=77),
            dmc.SegmentedControl(
                id=id_,
                value=value,
                data=data,
                w=width,
            ),
        ]
    )
