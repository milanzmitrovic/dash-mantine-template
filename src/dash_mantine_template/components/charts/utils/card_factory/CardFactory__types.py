### ### ### CardFactory Types ### ### ###

"""

Purpose of this function is to organize code that
will be used for holding info about component IDs
that are used in CardFactory component.

"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ShadowRadiusTypes(str, Enum):
    """

    Purpose of this function is to keep
    possible values that shadow, radius
    or type can have.

    """

    xs = "xs"
    sm = "sm"
    md = "md"
    xl = "xl"
    lg = "lg"


class Shadow(BaseModel):
    """

    Purpose of this function is to keep
    all possible values that SHADOW
    property can take.

    """

    value: ShadowRadiusTypes


class Radius(BaseModel):
    """

    Purpose of this function is to keep
    all possible values that RADIUS
    property can take.

    """

    value: ShadowRadiusTypes


class Width(BaseModel):
    """

    Purpose of this function is to keep
    all possible values that WIDTH
    property can take.

    """

    value: Optional[int]


class Height(BaseModel):
    """

    Purpose of this function is to keep
    all possible values that HEIGHT
    property can take.

    """

    value: Optional[int]


class Margin(BaseModel):
    """

    Purpose of this function is to keep
    all possible values that MARGIN
    property can take.

    """

    ml: int
    mr: int
    mb: int
    mt: int


class Padding(BaseModel):
    """

    Purpose of this function is to keep
    all possible values that MARGIN
    property can take.

    """

    pl: int
    pr: int
    pb: int
    pt: int


class ChartTitle(BaseModel):
    """

    Purpose of this function is to keep
    all possible values that ChartTitle
    property can take.

    """

    value: str
