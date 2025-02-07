"""

Purpose of this file is to
organize logic for testing
functionalities related to
implementation of create app
pattern in template project.

"""

import dash

from dash_mantine_template.utils.CreateApp import create_app


def test__create_app():
    """
    Purpose of this test is to
    confirm that Dash app is
    actually created by create
    app factory pattern.
    """

    assert isinstance(create_app(), dash.Dash)
