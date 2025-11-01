"""

"""
import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call
from typing import TypedDict, List, Optional


class TechOption(TypedDict):
    value: str
    label: str


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def select(
    id: str,
    value: str,
    data: List[TechOption],
    width: Optional[int] = 200,
    m: Optional[int] = 20,
    label: Optional[str] = None,
):
    return dmc.Select(
            id=id,
            label=label,
            value=value,
            data=data,
            w=width,
            m=m
        )
