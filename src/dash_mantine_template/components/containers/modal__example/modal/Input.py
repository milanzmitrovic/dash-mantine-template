"""
Here we define all INPUT elements
of callback for modal_example
component.

These components will be used in
CallbackSignature.py files.

All components that depend on
modal_example component (i.e.
have it as input/state dependency)
will use these functions in their
CallbackSignature.py file.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def input_():
    """
    This will be used in all components that
    depend on modal_example component i.e.
    in all components that have modal_example
    as input/state dependency.

    This typically triggers when modal opens/closes.
    Default property is 'opened'.
    """
    return gc.modal.input_(id_=ID.modal)
