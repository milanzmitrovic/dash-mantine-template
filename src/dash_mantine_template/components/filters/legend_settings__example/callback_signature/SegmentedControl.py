"""
Purpose of this file is to define callback
signature.
"""

from ..input import input_dummy
from ..output import output__data__legend_orientation


def inputs__all():
    """
    1
    """
    return {"dummy_input": input_dummy()}


def output__all():
    """
    2
    """
    return {
        "data": output__data__legend_orientation(),
        # 'value': dash.no_update
    }
