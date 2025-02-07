"""
Purpose of this file is to help with
organization of logic for mani component
in Dash Mantine template.

"""

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call

from ..DashPagesUtil import page_content, page_navigation_component


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def main_component() -> dmc.AppShellMain:
    """
    Purpose of this function is to create main
    component in Dash app.

    It will be wrapped around Mantine provider
    and it will hold main content of app.

    return: dmc.AppShellMain component.

    """
    return dmc.AppShellMain(children=[page_navigation_component(), page_content()])
