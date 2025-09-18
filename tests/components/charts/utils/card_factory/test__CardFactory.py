### ### ### Test CardFactory ### ### ###

""" """

import dash_mantine_components as dmc
import pytest

from dash_mantine_template.components.charts.utils.card_factory.CardFactory import (
    CardFactory,
)
from dash_mantine_template.components.charts.utils.card_factory.CardFactory__types import (
    ShadowRadiusTypes,
)


@pytest.fixture
def card_factory():
    """
    x
    """
    return CardFactory(chart_id="1", header_id="2")


def test_init(card_factory):
    assert card_factory.chart_id == "1"
    assert card_factory.header_id == "2"


def test_set_radius(card_factory):
    card_factory.set_radius(
        radius_header=ShadowRadiusTypes.xs.value, radius_body=ShadowRadiusTypes.xl.value
    )

    assert card_factory.radius_header == "xs"
    assert card_factory.radius_body == "xl"


def test_set_shadow(card_factory):
    card_factory.set_shadow(
        shadow_header=ShadowRadiusTypes.xs.value, shadow_body=ShadowRadiusTypes.xl.value
    )

    assert card_factory.shadow_header == "xs"
    assert card_factory.shadow_body == "xl"


def test_set_margin(card_factory):
    pass


def test_set_padding(card_factory):
    pass


def test_set_width(card_factory):
    pass


def test_set_height(card_factory):
    pass


def test_set_vertical_spacing(card_factory):
    card_factory.set_vertical_spacing(vertical_spacing=ShadowRadiusTypes.xs.value)

    assert card_factory.vertical_spacing == "xs"


def test_set_borders(card_factory):
    card_factory.set_borders(with_borders=True)

    assert card_factory.with_borders is True


def test_get_card(card_factory):
    card_factory.set_radius(
        radius_header=ShadowRadiusTypes.xs.value, radius_body=ShadowRadiusTypes.xl.value
    )

    card_factory.set_shadow(
        shadow_header=ShadowRadiusTypes.xs.value, shadow_body=ShadowRadiusTypes.xl.value
    )

    card_factory.set_border_style(style="1px solid #777777")

    card_factory.set_vertical_spacing(vertical_spacing=ShadowRadiusTypes.xs.value)
    card_factory.set_borders(with_borders=True)

    assert isinstance(card_factory.get_card(), dmc.SimpleGrid)

    assert len(card_factory.get_card().children) == 3
