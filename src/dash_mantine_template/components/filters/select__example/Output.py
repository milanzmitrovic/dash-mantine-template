"""
1
"""

from dash_mantine_template import gc
from .ComponentID import ID


def output__data():
    """
    1
    """
    return gc.multiselect.output(id_=ID.select)


def output__value():
    """
    1
    """
    return gc.select.output(id_=ID.select, property_='value')
