"""
Purpose of this file is to organize logic
that will be responsible for analytics page.
"""

import dash
from dash import (
    html,
)

from dash_mantine_template.components.filters.radio_button import (
    radio_button__component,
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
            radio_button__component(),
            html.Br(),
        ]
    )
