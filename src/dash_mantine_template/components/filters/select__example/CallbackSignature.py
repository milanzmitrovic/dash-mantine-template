"""
Purpose of this file is to define callback
signature.
"""

from .Input import input_dummy
from .Output import output__data, output__value
from .Running import running


def inputs__all():
    """
    This function is defining input part of
    callback signature.

    All input components triggering callback
    are instantiated here.
    """
    return {"dummy_input": input_dummy()}


def output__all():
    """
    This function is defining output part of
    callback signature.

    All output components are instantiated here.
    """
    return {
        "data": output__data(),
        "value": output__value(),
        # 'loading_overlay': output__loading_overlay(),
    }


def running__all():
    """
    This function is defining running part of
    callback signature.
    """
    return running()
