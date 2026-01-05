"""
Here we define all INPUT elements
of callback for pagination_example
component.

These components will be used in
CallbackSignature.py files.

All components that depend on
pagination_example component (i.e.
have it as input/state dependency)
will use these functions in their
CallbackSignature.py file.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def input_dummy():
    """
    This will be typically used ONLY in callback
    that is setting initial values to UI component.

    Values are queried from database.

    Component properties such as <total>, <value>
    will be updated initially via callback.
    """
    return gc.pagination.input_dummy(id_=ID.pagination)


def input_():
    """
    This will be used in all components that
    depend on pagination_example component i.e.
    in all components that have pagination_example
    as input/state dependency.

    This typically triggers when user clicks on a page number.
    """
    return gc.pagination.input_(id_=ID.pagination)
