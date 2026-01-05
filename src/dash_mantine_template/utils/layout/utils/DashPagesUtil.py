"""
Purpose of this file is to keep logic
for functions and components that are
consumed by Dash pages functionality.
"""

import dash
import dash_mantine_components as dmc
from dash import Input, Output, clientside_callback, dcc, html
from pydantic import ConfigDict, validate_call

from ....component_ids.utils.layout.Layout import (
    location_url__id,
    location_url_property,
)
from ....component_ids.utils.layout.utils.DashPagesUtil import (
    tabs__id,
    tabs__property,
)


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def page_content() -> html.Div:
    """
    Purpose of this component is to work as
    placeholder for content that will be
    created by switching between Dash pages.

    It should be strictly used in main component
    of AppShell provider.

    return: dash page container object.

    """

    return dash.page_container


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def page_navigation_tab(name: str, link: str) -> dcc.Link:
    """

    Purpose of this function is to create single TAB
    that will be later shown on page navigation
    component.

    Inputs:
        name - Text that will be shown on tab button.
        link - Location that browser will be taken to
               after user clicks on tab button.

    return: dcc.Link() with dmc.TabsTab() inside itself.
    """

    # Most important thing here is to put dmc.TabsTab() inside
    # dcc.Link() and NOT vice verse. Why?
    # If we put it vice verse, then dcc.Link() will work only
    # when link is clicked. But, if we do it properly (by putting
    # dmc.TabsTab() inside dcc.Link(), then link will work whenever
    # we click inside tab, regardless if we clicked on link or
    # outside link).
    return dcc.Link(
        children=dmc.TabsTab(
            html.Div(name),
            value=link,
        ),
        href=link,
        style={
            "textDecoration": "none",  # Removes underline
            "color": "inherit",  # Inherits color from parent
        },
    )


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def page_navigation_component() -> dmc.Container:
    """
    Purpose of this function is to create component that
    will hold TABs and display them to user.

    return: htm.Div containing component.
    """
    return dmc.Container(
        [
            html.Br(),
            html.Br(),
            dmc.Tabs(
                id=tabs__id.id,
                children=[
                    dmc.TabsList(
                        [
                            page_navigation_tab(
                                name=f"{page['name']}", link=page["relative_path"]
                            )
                            for page in dash.page_registry.values()
                        ],
                        justify="center",
                        variant="outline",
                    )
                ],
                color="red",  # default is blue
                orientation="horizontal",  # or "vertical"
                variant="default",  # or "outline" or "pills"
                value="/",  # Active TAB by default
            ),
        ],
        # When new pages are added,
        # size should be increased.
        size=310,
    )


# When user clicks on specific TAB,
# it will become active (i.e. it will
# become underlined with red horizontal
# arrow).
# But, what if user user clicked on
# hyperlink that he/she got from colleague?
# Then, TAB button will not be highloghted.
# This is why callback below is important.
# It will check TAB's state whenever URL is
# changed. So, we are 100% sure that proper
# TAB will always be highlighted.
clientside_callback(
    """
    function(pathname) {
        return pathname
    }
    """,
    Output(tabs__id.id, tabs__property.value),
    Input(location_url__id.id, location_url_property.pathname),
)
