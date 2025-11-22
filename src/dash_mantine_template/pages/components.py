"""
1
"""

import dash
import dash_mantine_components as dmc
from dash import html

from dash_mantine_template.components.containers.modal__example import button, modal
from dash_mantine_template.components.filters import (
    button__example,
    date_input__example,
    legend_settings__example,
    multiselect__example,
    number_input__example,
    radio_button__example,
    segmented_control__example,
    select__example,
)
from dash_mantine_template.components.miscellaneous import pagination__example

dash.register_page(__name__, path="/components")


def layout():
    """
    Purpose of this function is to create
    main layout component of home page.
    """
    return html.Div(
        [
            html.Br(),
            dmc.SimpleGrid(
                [
                    radio_button__example.component(),
                    number_input__example.component(),
                    button__example.component(),
                    multiselect__example.component(),
                    select__example.component(),
                    segmented_control__example.component(),
                    legend_settings__example.component(),
                    pagination__example.component(),
                    date_input__example.component(),
                    button.component(),
                    modal.component(),
                ],
                cols=2,
            ),
            html.H1("This is our: Components page"),
            html.Div("This is our Components page content."),
        ]
    )
