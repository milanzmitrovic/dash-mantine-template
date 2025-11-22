"""
1
"""

from dash import html

# Can't import gc from dash_mantine_template;
# There is circular import error.
from dash_mantine_template.utils.global_components.basic_components import (
    number_input,
    radio_button,
    segmented_control,
)


def component(id_: str):
    """
    1
    """

    # data__legend_location = [
    #     {'value': 'top-left', 'label': 'Top Left'},
    #     {'value': 'top-right', 'label': 'Top Right'},
    #     {'value': 'bottom-left', 'label': 'Bottom Left'},
    #     {'value': 'bottom-right', 'label': 'Bottom Right'}
    # ]
    #
    # data__legend_orientation = [
    #     {'value': 'horizontal', 'label': 'Horizontal'},
    #     {'value': 'vertical', 'label': 'Vertical'}
    # ]

    return html.Div(
        children=[
            # Dummy input
            html.Div(id=id_ + "_dummy-input", n_clicks=77),
            # Top/Bottom, Left/Right
            radio_button.component(
                id_=id_ + "__legend_location", children=html.Div([])
            ),
            # Horizontal/Vertical
            segmented_control.component(id_=id_ + "__legend_orientation", data=[]),
            # position_x, position_y
            number_input.component(id_=id_ + "__position_x", label="Position X"),
            number_input.component(id_=id_ + "__position_y", label="Position Y"),
        ]
    )
