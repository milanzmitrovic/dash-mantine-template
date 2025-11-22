"""
Here we define all OUTPUT elements
of callback for modal_example
component.

These components will be used in
CallbackSignature.py files.

Here we instantiate components that
are defining attributes which are
updated via callback.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def output__opened():
    """
    Here we instantiate <opened> property of
    component that is being updated via callback.

    This controls whether the modal is visible.
    External components (like button__example) will
    update this property to open/close the modal.
    """
    return gc.modal.output(id_=ID.modal)
