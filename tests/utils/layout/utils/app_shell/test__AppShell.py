"""

Purpose of this file is to
organize logic for testing
Mantine AppShell functionalities.

"""

import dash_mantine_components as dmc

from dash_mantine_template.utils.layout.utils.app_shell.AppShell import app_shell


def test__app_shell():
    """
    Purpose of this function is to
    test component that is creating
    dmc.AppShell component.
    """

    assert isinstance(app_shell(content=[]), dmc.AppShell)
