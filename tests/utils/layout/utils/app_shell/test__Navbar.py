"""

Purpose of this file is to
organize logic for testing
Mantine AppShellNavbar functionalities.

"""

import dash_mantine_components as dmc

from dash_mantine_template.utils.layout.utils.app_shell.Navbar import navbar_component


def test__navbar_component():
    """
    Purpose of this function is to
    test component that is creating
    dmc.AppShellNavbar component.
    """

    assert isinstance(navbar_component(), dmc.AppShellNavbar)
