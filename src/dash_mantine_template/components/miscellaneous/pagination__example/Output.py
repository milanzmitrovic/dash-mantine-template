"""
Here we define all OUTPUT elements
of callback for pagination_example
component.

These components will be used in
CallbackSignature.py files.

Here we instantiate components that
are defining attributes which are
updated via callback.
"""

from dash_mantine_template import gc

from .ComponentID import ID


def output__total():
    """
    Here we instantiate <total> property of
    component that is being updated via callback.

    This is typically set based on data size
    and items per page (e.g., total_pages = ceil(total_items / items_per_page))
    """
    return gc.pagination.output(id_=ID.pagination, property_="total")


def output__value():
    """
    Here we instantiate <value> property of
    component that is being updated via callback.

    This represents the current active page.
    """
    return gc.pagination.output(id_=ID.pagination, property_="value")
