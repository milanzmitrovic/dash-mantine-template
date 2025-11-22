"""
Purpose of this file is to hold number_input
UI component.
"""

import dash_mantine_components as dmc
from typing import Optional, Literal
from pydantic import validate_call, ConfigDict
from .Types import Size, Radius


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def component(
        id_: str,
        value: Optional[str] =None,
        placeholder: Optional[str] =None,
        label: Optional[str] =None,
        size: Optional[Size] =None,
        radius: Optional[Radius] =None,
        disabled: bool =False,
        width: Optional[int] = None
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
        w=width
    )
