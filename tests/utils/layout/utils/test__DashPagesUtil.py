"""

Purpose of this file is to organize tests
related with utility functions necessary
for proper function of Dash template app.

"""

import dash_mantine_components as dmc
from dash import dcc, html

from dash_mantine_template.utils.Layout.utils.DashPagesUtil import (
    page_content,
    page_navigation_component,
    page_navigation_tab,
)


def test__page_content():
    """
    Purpose of this function is
    to test returned type of
    page content object.
    """

    assert isinstance(page_content(), html.Div)


def test__page_content__not_equal():
    """
    Purpose of this function is
    to test returned type of
    page content object using
    not equal condition.
    """

    assert not isinstance(page_content(), html.Button)


# --- --- --- #


def test__page_navigation_component():
    """
    Purpose of this function is to
    test component that will have
    tabs showing pages in itself.
    """

    assert isinstance(page_navigation_component(), dmc.Container)


# --- --- --- #


def test__page_navigation_tab():
    """
    Purpose of this function is to
    make sure that dmc.TabsTab components
    are inside dcc.Link parent component.

    Why is that important? Because we want
    to make tab clickable on its entire area,
    not only on when text is clicked.
    """

    assert isinstance(page_navigation_tab(name="test_name", link="test_link"), dcc.Link)


def test__page_navigation_tab__child_element():
    """
    Purpose of this function is to
    make sure that inside dcc.Link
    component there are dmc.TabsTab
    components.
    """

    assert isinstance(
        page_navigation_tab(name="test_name", link="test_link").children, dmc.TabsTab
    )
