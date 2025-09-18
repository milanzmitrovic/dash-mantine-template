"""

Purpose of this file is to
organize logic for testing
Mantine AppShellHeader functionalities.

"""

import dash_mantine_components as dmc

from dash_mantine_template.utils.layout.utils.app_shell.Header import header_component


def test__header_component():
    """
    Purpose of this function is to
    test component that is creating
    dmc.AppShellHeader component.
    """

    assert isinstance(header_component(), dmc.AppShellHeader)
