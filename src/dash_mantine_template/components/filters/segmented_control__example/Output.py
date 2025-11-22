"""
1
"""

from dash_mantine_template import gc
from .ComponentID import ID


def output__data():
    """
    1
    """
    return gc.multiselect.output(id_=ID.segmented_control)


def output__value():
    """
    1
    """
    return gc.segmented_control.output(id_=ID.segmented_control, property_='value')
