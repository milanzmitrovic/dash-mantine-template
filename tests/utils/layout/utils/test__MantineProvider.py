"""

Purpose of this file is to
organize tests related with
Mantine provider component.

"""

import dash_mantine_components as dmc

from dash_mantine_template.utils.layout.utils.MantineProvider import mantine_provider


def test__mantine_provider():
    """
    Purpose of this function is to
    test component that is creating
    Mantine provider object.
    """

    assert isinstance(mantine_provider(content=[]), dmc.MantineProvider)
