"""
Purpose of this file is to organize logic
that will be responsible for home page.
"""

import dash
from dash import html

dash.register_page(__name__, path="/")


def layout():
    """
    Purpose of this function is to create
    main layout component of home page.
    """
    return html.Div(
        [
            html.H1("This is our: Home page"),
            html.Div("This is our Home page content."),
        ]
    )
