"""
Purpose of this file is to hold modal
UI component.
"""

from typing import Any, Optional

import dash_mantine_components as dmc
from dash import html
from pydantic import ConfigDict, StrictInt, validate_call


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(
    id_: str,
    children: Any,
    opened: bool = False,
    title: Optional[str] = None,
    size: Optional[str | StrictInt] = "md",
    centered: Optional[bool] = True,
):
    """
    UI function returning modal component.

    Modal is controlled externally via 'opened' property.
    No button is included in the component itself.

    Parameters:
    - id_: Component identifier
    - children: Content to display inside the modal
    - opened: Whether the modal is opened (controlled externally)
    - title: Modal title
    - size: Modal size (xs, sm, md, lg, xl, or pixel value)
    - centered: Whether to center the modal vertically
    """

    return html.Div(
        [
            dmc.Modal(
                id=id_,
                opened=opened,
                title=title,
                size=size,
                centered=centered,
                children=children,
            ),
        ]
    )
