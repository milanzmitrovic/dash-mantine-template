"""
Purpose of this file is to organize logic
that will be responsible for analytics page.
"""

import dash
from dash import (
    html,
)
from dash_mantine_template import cc

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
            cc.button(text="ydbehdbed", id='123'),
            cc.select(
                id='fdefe',
                value='torch',
                data=[
                {"value": "pd", "label": "Pandas"},
                {"value": "np", "label": "NumPy"},
                {"value": "tf", "label": "TensorFlow"},
                {"value": "torch", "label": "PyTorch"},
            ],

            ),
            html.H1("This is our: Analytics page"),
            radio_button__component(),
            html.Br(),
        ]
    )
