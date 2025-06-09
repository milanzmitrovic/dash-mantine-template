"""
Purpose of this file is to organize
logic for for creating Mantine
provider component.

It is one of main building blocks
of app template. All other components
will live inside Mantine provider.

Also, this will enable Mantine styles
to be applied to all elements inside
Dash app.
"""

from typing import List

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def mantine_provider(content: List) -> dmc.MantineProvider:
    """
    Purpose of this function is to put elements
    inside Mantine provides.

    Input
        - content: List with elements toat should
        be put inside Mantine provider.

    :return: dmc.MantineProvider component.
    """
    return dmc.MantineProvider(
        children=content,
        forceColorScheme="dark",
    )
