"""
1
"""

import dash
from dash import html
from dash_mantine_template.components.filters import radio_button__example
from dash_mantine_template.components.filters import number_input__example
from dash_mantine_template.components.filters import button__example
from dash_mantine_template.components.filters import multiselect__example
from dash_mantine_template.components.filters import select__example
from dash_mantine_template.components.filters import segmented_control__example

import dash_mantine_components as dmc

dash.register_page(__name__, path="/components")


def layout():
    """
    Purpose of this function is to create
    main layout component of home page.
    """
    return html.Div(
        [

            html.Br(),

            dmc.SimpleGrid([
                radio_button__example.component(),

                number_input__example.component(),

                button__example.component(),

                multiselect__example.component(),

                select__example.component(),

                segmented_control__example.component()

            ],
            cols=2
            ),

            html.H1("This is our: Components page"),
            html.Div("This is our Components page content."),
        ]
    )
