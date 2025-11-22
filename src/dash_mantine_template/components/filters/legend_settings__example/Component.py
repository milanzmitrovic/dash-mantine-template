"""
Purpose of this file is to define UI
component that will be used in app.
"""

import dash_mantine_components as dmc

from dash_mantine_template import gc

from .callback.PositionXY import *  # noqa: F403
from .callback.RadioButton import *  # noqa: F403
from .callback.SegmentedControl import *  # noqa: F403
from .ComponentID import ID


def component():
    """
    1
    """

    return dmc.Container(
        children=[gc.legend_settings.component(id_=ID.legend_settings)], w=500
    )
