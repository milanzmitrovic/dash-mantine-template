"""
Purpose of this file is to organize
logic related with select component.
"""

from dash import Input, Output, callback, dcc, html
from pydantic import ConfigDict, validate_call

from ...component_ids.filters.select_component import (
    SelectComponent__ID,
    SelectComponent__Property,
    output_component__id,
    output_component__property,
)


def radio_button__component():
    """
    Create select component that will
    be visible by user.
    """
    return html.Div(
        [
            "Select a city: ",
            dcc.RadioItems(
                options=[
                    "New York City",
                    "Montreal",
                    "San Francisco",
                ],
                value="Montreal",
                id=SelectComponent__ID.id,
            ),
            html.Div(id=output_component__id.id),
        ]
    )


@callback(
    Output(output_component__id.id, output_component__property.children),
    Input(SelectComponent__ID.id, SelectComponent__Property.value),
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def update_city_selected(input_value: str):
    """
    Purpose of this function is to handle
    interactive logic that is connected to
    select component.
    """
    return f"You selected: {input_value}"
