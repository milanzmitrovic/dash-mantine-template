"""

Purpose of this file is to organize logic
for entire AppShell component.

It is parent component that will hold
other components inside itself:
    - Main
    - Header
    - Navbar
    - Aside

"""

from typing import List

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def app_shell(content: List) -> dmc.AppShell:
    """
    Purpose of this function is to put
    elements inside dmc.AppShell parent
    component.

    :return dmc.AppShell component.
    """
    return dmc.AppShell(children=content)
