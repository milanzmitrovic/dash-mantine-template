"""
Here we define all INPUT elements
of callback for button_example
component.

These components will be used in
CallbackSignature.py files.

All components that depend on
button_example component (i.e.
have it as input/state dependency)
will use these functions in their
CallbackSignature.py file.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def input_():
    """
    This will be used in all components that
    depend on button_example component i.e.
    in all components that have button_example
    as input/state dependency.

    This triggers when the button is clicked.
    Default property for button is 'n_clicks'.
    """
    return gc.button.input_(id_=ID.button)
