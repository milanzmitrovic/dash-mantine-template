"""
Purpose of this file is to organize logic
that will be responsible for analytics page.
"""

import dash
from dash import (
    html,
)


dash.register_page(__name__, path="/analytics")


def layout():
    """
    Purpose of this function is to create
    main layout component of analytics page.
    """
    return html.Div(
        [
            html.H1("This is our: Analytics page"),
            html.Br(),
        ]
    )
