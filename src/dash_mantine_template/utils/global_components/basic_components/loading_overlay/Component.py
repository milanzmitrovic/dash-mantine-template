"""
1
"""

from typing import List, Optional

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call


@validate_call(
    config=ConfigDict(arbitrary_types_allowed=True, strict=True), validate_return=True
)
def component(id_: str, children: Optional[List] = None):
    """
    1
    """

    loading_overlay__list = [
        # This should be first element in list.
        # It will cover all other elements while
        # app is loading i.e. while callback is
        # being processed.
        dmc.LoadingOverlay(
            visible=True,
            id=id_ + "__loading-overlay",
            overlayProps={"radius": "sm", "blur": 2},
            zIndex=10,
        )
    ]

    if children is not None:
        # Append all other elements that are provided
        # by user i.e. elements that should be hidden
        # behind dmc.LoadingOverlay().
        final_children = loading_overlay__list + children

    else:
        final_children = loading_overlay__list

    return dmc.Box(
        children=[
            dmc.Stack(
                pos="relative",
                p=5,
                w=300,
                children=final_children,
            ),
        ]
    )
