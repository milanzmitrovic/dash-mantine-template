"""
Purpose of this file is to help
with organization of logic that
will be put on the LEFT side of
main application view.

Left side of page.

"""

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def navbar_component() -> dmc.AppShellNavbar:
    """
    Purpose of this function is to
    create Mantine component that
    will be shown on LEFT side of
    view.

    :return dmc.AppShellNavbar component.
    """
    return dmc.AppShellNavbar(["555"])
