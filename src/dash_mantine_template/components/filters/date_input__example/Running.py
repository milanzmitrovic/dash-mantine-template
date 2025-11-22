"""
Purpose of this file is to help with
instantiation of callback component.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def running():
    """
    Here we instantiate running component
    that will be used in callback signature.
    """

    return gc.loading_overlay.running_(id_=ID.date_input)
