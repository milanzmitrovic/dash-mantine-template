"""
Purpose of this file is to hold pagination
UI component.
"""

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
    value: StrictInt,
    total: StrictInt,
    siblings: Optional[StrictInt] = None,
    boundaries: Optional[StrictInt] = None,
    size: Optional[str] = None,
    radius: Optional[str] = None,
):
    """
    UI function returning pagination
    component.

    Parameters:
    - id_: Component identifier
    - value: Current active page (1-indexed)
    - total: Total number of pages
    - siblings: Number of siblings on each side of current page
    - boundaries: Number of always visible pages at the start and end
    - size: Component size (xs, sm, md, lg, xl)
    - radius: Border radius (xs, sm, md, lg, xl)
    """

    return html.Div(
        [
            # This component will be used to trigger
            # initial enrichment of component with
            # fresh data from database.
            dummy_input.component(id_=id_),
            dmc.Pagination(
                id=id_,
                value=value,
                total=total,
                siblings=siblings,
                boundaries=boundaries,
                size=size,
                radius=radius,
            ),
        ]
    )
