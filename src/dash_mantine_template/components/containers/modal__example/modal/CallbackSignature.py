"""
Purpose of this file is to define callback
signature.
"""

from .. import button
from .Output import output__opened


def inputs__all():
    """
    This function is defining input part of
    callback signature.

    All input components triggering callback
    are instantiated here.
    """
    return {"dummy_input": button.input_()}


def output__all():
    """
    This function is defining output part of
    callback signature.

    All output components are instantiated here.
    """
    return {
        "opened": output__opened(),
    }
