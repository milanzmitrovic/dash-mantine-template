"""

Purpose of this file is to
organize logic for testing
Mantine AppShellAside functionalities.

"""

import dash_mantine_components as dmc

from dash_mantine_template.utils.layout.utils.app_shell.Aside import aside_component


def test__aside_component():
    """
    Purpose of this function is to
    test component that is creating
    dmc.AppShellAside component.
    """

    assert isinstance(aside_component(), dmc.AppShellAside)
