"""
Purpose of this file is to
organize logic for testing
functionality of radio
button.
"""

from dash import html

from dash_mantine_template.components.filters.radio_button import (
    radio_button__component,
    update_city_selected,
)


def test__radio_button__component():
    assert isinstance(radio_button__component(), html.Div)


def test__update_city_selected():
    test_input_value = "test_city"

    assert (
        update_city_selected(input_value=test_input_value)
        == f"You selected: {test_input_value}"
    )
