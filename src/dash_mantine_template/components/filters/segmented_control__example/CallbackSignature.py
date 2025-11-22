"""
1
"""
from .Input import input_dummy
from .Output import output__data, output__value


def inputs__all():
    """
    1
    """
    return {
        'dummy_input': input_dummy()
    }


def output__all():
    """
    2
    """
    return {
        'data': output__data(),
        'value': output__value()
    }
