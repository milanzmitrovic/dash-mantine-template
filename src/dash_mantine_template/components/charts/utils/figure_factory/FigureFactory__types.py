"""

Purpose of this module is to organize
IDs for components used inside FigureFactory
class and module.

"""

from enum import Enum

import plotly.graph_objects as go
from pydantic import BaseModel


class Figure(BaseModel):
    """
    Holds type of dcc.Graph() component.

    """

    value: go.Figure

    class Config:
        arbitrary_types_allowed = True


class BackgroundColor(str, Enum):
    """
    This class hold possible values that
    background color property can take.

    """

    dark = "dark"
    light = "light"


class LegendPosition(str, Enum):
    """
    This class hold possible values that
    legend position can have.

    """

    TOP = "top"
    BOTTOM = "bottom"


class ValueStyle(str, Enum):
    """
    This class hold possible values that
    number style property can take.

    """

    THOUSANDS = "thousands"
    K_NOTATION = "k_notation"
