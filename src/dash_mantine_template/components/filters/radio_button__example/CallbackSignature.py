"""
1
"""
from .Input import input_dummy
from .Output import output__children, output__value


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
        'children': output__children(),
        'value': output__value()
    }
