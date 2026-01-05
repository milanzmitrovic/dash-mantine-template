"""
Purpose of this file is to define callback
signature.
"""

from ..input import input__radio_button__legend_location
from ..output import output__value__pixel_x, output__value__pixel_y


def inputs__all():
    """
    1
    """
    return {"legend_location": input__radio_button__legend_location()}


def output__all():
    """
    2
    """
    return {"pixel_x": output__value__pixel_x(), "pixel_y": output__value__pixel_y()}
