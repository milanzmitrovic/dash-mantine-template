""" """

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def button(
    text: str,
    id: str,
    color: str = "blue",
    size: str = "sm",
    variant: str = "filled",
    radius: str = "sm",
    loading: bool = False,
    disabled: bool = False,
):
    """
    1
    """
    return dmc.Button(
        id=id,
        children=text,
        color=color,
        variant=variant,
        size=size,
        radius=radius,
        loading=loading,
        disabled=disabled,
        # other props...
    )
