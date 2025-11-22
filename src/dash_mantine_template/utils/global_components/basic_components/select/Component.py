"""
Purpose of this file is to hold multiselect
UI component.
"""

from typing import List, Optional

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, StrictInt, validate_call

from .. import dummy_input
from .Types import DataDict


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(
    id_: str,
    value: str,
    data: DataDict | List,
    label: Optional[str] = None,
    placeholder: Optional[str] = None,
    width: Optional[StrictInt] = None,
):
    """
    UI function returning multiselect
    component.
    """

    return html.Div(
        [
            # This component will be used to trigger
            # initial enrichment of component with
            # fresh data from database.
            dummy_input.component(id_=id_),
            dmc.Select(
                id=id_,
                value=value,
                label=label,
                placeholder=placeholder,
                data=data,
                w=width,
            ),
        ]
    )
