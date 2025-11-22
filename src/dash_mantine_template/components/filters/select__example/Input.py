"""
Here we define all INPUT elements
of callback for select_example
component.

These components will be used in
CallbackSignature.py files.

All components that depends on
select_example component (i.e.
have it as input/state dependency)
will use these functions its
CallbackSignature.py file.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def input_dummy():
    """
    This will be typically used ONLY in callback
    that is setting initial values to UI component.

    Values are queried from database.

    Component properties such as <data>, <value>
    will be updated initially via callback.
    """
    return gc.select.input_dummy(id_=ID.select)


def input_():
    """
    This will be used in all components that
    depend on select_example component i.e.
    in all components that have select_example
    as input/tate dependency.
    """
    return gc.select.input_(id_=ID.select)


# def running():
#     """
#     1
#     """
#
#     return gc.select.running(id_=ID.select)
#
