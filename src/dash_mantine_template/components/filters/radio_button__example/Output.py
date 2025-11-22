"""
1
"""

from dash_mantine_template import gc
from .ComponentID import ID


def output__children():
    """
    1
    """
    return gc.radio_button.output(id_=ID.legend_position)


def output__value():
    """
    1
    """
    return gc.radio_button.output(id_=ID.legend_position, property_='value')
