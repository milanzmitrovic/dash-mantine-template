"""
Purpose of this file is to define callback
signature.
"""

from .Input import input_dummy
from .Output import output__data, output__value
from .Running import running


def inputs__all():
    """
    1
    """
    return {"dummy_input": input_dummy()}


def output__all():
    """
    2
    """
    return {"data": output__data(), "value": output__value()}


def running__all():
    """
    1
    """
    return running()
