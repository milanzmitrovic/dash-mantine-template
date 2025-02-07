"""

Purpose of this file is to
organize logic for testing
Mantine AppShellMain functionalities.

"""

import dash_mantine_components as dmc

from dash_mantine_template.utils.layout.utils.app_shell.Main import main_component


def test__main_component():
    """
    Purpose of this function is to
    test component that is creating
    dmc.AppShellMain component.
    """

    assert isinstance(main_component(), dmc.AppShellMain)
