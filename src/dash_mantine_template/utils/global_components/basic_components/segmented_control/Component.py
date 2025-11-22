"""
Purpose of this file is to hold multiselect
UI component.
"""

from typing import List, Optional

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, validate_call

from .. import dummy_input
from .Types import DataDict


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component(
    id_: str,
    data: List[DataDict] | List,
    value: Optional[str] = None,
    width: Optional[int] = None,
):
    """
    UI function returning multiselect
    component.
    """

    return html.Div(
        children=[
            dummy_input.component(id_=id_),
            dmc.SegmentedControl(
                id=id_,
                value=value,
                data=data,
                w=width,
            ),
        ]
    )
