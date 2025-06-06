"""
Purpose of this file is to
organize logic for header
component of Dash app.

Top of the page.

"""

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def header_component() -> dmc.AppShellHeader:
    """
    Purpose of this function is to
    create component that will be
    on top of page view.

    It will be component from
    Mantine library.

    :return dmc.AppShellHeader component.
    """
    return dmc.AppShellHeader(
        children=[dmc.Center("Dash Mantine Template - Header component")]
    )
