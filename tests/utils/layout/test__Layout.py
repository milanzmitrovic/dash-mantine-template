"""
Purpose of this file is to organize
tests that are related to app's
layout component.
"""

import dash_mantine_components as dmc

from dash_mantine_template.utils.Layout.Layout import layout


def test__layout():
    """
    Perform testing of app's
    layout component.
    """
    assert isinstance(layout(), dmc.MantineProvider)
