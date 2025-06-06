"""
Purpose of this file is to help with
organization of 'create app' pattern.
"""

import dash
from dash import Dash
from flask import Flask
from pydantic import ConfigDict, validate_call

from .layout.Layout import layout


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def create_app() -> dash.Dash:
    """
    Purpose of this function is to
    create Dash app and to attach
    layout to Dash app.

    Things that are done here:
        - Create Flask server.
        - Set location of Dash
        pages folder.
        - Set title of app.
        - Attach layout to main
        Dash application.

    :return: dash.Dash app that should
             be run as main function.
    """
    flask_server = Flask(__name__)

    dash_app = Dash(
        __name__,
        use_pages=True,
        title="Dash Mantine Template",
        # Necessary because pages folder is in root,
        # while app is instantiated in child folder.
        pages_folder="../",
        server=flask_server,
    )

    dash_app.layout = layout()

    return dash_app
