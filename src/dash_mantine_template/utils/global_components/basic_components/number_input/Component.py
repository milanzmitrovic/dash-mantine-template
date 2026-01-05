"""
Purpose of this file is to hold number_input
UI component.
"""

from typing import Optional

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call

from .Types import Radius, Size


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component(
    id_: str,
    value: Optional[str] = None,
    placeholder: Optional[str] = None,
    label: Optional[str] = None,
    size: Optional[Size] = None,
    radius: Optional[Radius] = None,
    disabled: bool = False,
    width: Optional[int] = None,
) -> dmc.NumberInput:
    """
    UI function returning number_input
    component.
    """

    return dmc.NumberInput(
        id=id_,
        value=value,
        placeholder=placeholder,
        label=label,
        size=size,
        radius=radius,
        disabled=disabled,
        w=width,
    )
