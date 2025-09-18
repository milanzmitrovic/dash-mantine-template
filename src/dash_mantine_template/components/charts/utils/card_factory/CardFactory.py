### ### ### CardFactory ### ### ###

"""
Purpose of this file is to store class that
will be responsible for creating object in
which chart lives.

In simple words, dmc.Card() or dmc.Paper()
component should be created around Plotly
figure.

There should be methods for adjusting
styling of box (dmc.Paper() or dmc.Card()).

This class should be instantiated and used
closed to layout file.


Features present ATM:
    - set_radius() --> Set radius of dmc.Paper() component.
    - set_shadow() --> Set shadow of dmc.Paper() component.
    - set_vertical_spacing() --> Set spacing between two boxes - header and body.
    - set_borders() --> Purpose of this method is to put rectangle around
                        dmc.Container() object.
    - set_border_style() --> Set style of dmc.Paper() borderline.
    - get_card() --> Output of this function should be returned to
                    browser as callback output.

Planned features:
    - set_margin() --> Set margin around dmc.Paper() component.
    - set_padding() --> Set padding around dmc.Paper() component.
    - set_width() --> Set width of dmc.Paper() component explicitly.
    - set_height() --> Set height of dmc.Paper() component explicitly.

"""

from typing import Optional

import dash_mantine_components as dmc
import plotly.graph_objects as go
from dash import dcc, html
from pydantic import ConfigDict, validate_call

from dash_mantine_template.components.charts.utils.card_factory.CardFactory__types import (
    ShadowRadiusTypes,
)


class CardFactory:
    """

    Purpose of this function is to organize logic
    for creating chard component that will be
    responsible for holding charts created
    by application.

    """

    # Write here variables that will be used
    # in class. It helps prevent PyCharm/VSCode
    # warnings.
    with_borders: bool
    radius_header: ShadowRadiusTypes
    radius_body: ShadowRadiusTypes
    shadow_header: ShadowRadiusTypes
    shadow_body: ShadowRadiusTypes
    vertical_spacing: ShadowRadiusTypes | int
    border_style: dict

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def __init__(
        self,
        chart_id: str,
        header_id: Optional[str] = None,
        header_content: Optional[html.Div] = None,
        hidden_content: Optional[html.Div] = None,
    ):
        """
        Parameters:

            chart_id:   Will be used for callback to update
                        chart based on new data.

            header_id:  Necessary for updating color of header
                        component (in case header_content is
                        not None).

            header_content: Elements that should be shown in
                            header of card component. In other
                            words, it will be dmc.Paper()
                            component shown on top of dmc.Paper()
                            that is holding chart.

            hidden_content: Used to store things that should
                            not be visible to users. For example,
                            outputs of some callbacks that are not
                            used, but are necessary to be defined
                            (due to way how Dash callback logic
                            is designed - you need to have at least
                            one input and one output for each callback).

        """
        self.chart_id = chart_id
        self.header_id = header_id
        self.header_content = header_content
        self.hidden_content = hidden_content

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_radius(
        self,
        radius_header: Optional[ShadowRadiusTypes] = None,
        radius_body: Optional[ShadowRadiusTypes] = None,
    ):
        """
        Purpose of this function is to set RADIUS for
        both box like components - header and body.
        """
        self.radius_header = radius_header
        self.radius_body = radius_body

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_shadow(
        self,
        shadow_header: Optional[ShadowRadiusTypes],
        shadow_body: Optional[ShadowRadiusTypes],
    ):
        """
        Purpose of this function is to set SHADOW for
        both box like components - header and body.
        """
        self.shadow_header = shadow_header
        self.shadow_body = shadow_body

    def set_margin(self):
        """
        TODO:
        """
        pass

    def set_padding(self):
        """
        TODO:
        """
        pass

    def set_width(self):
        """
        TODO:
        """
        pass

    def set_height(self):
        """
        TODO:
        """
        pass

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_vertical_spacing(self, vertical_spacing: ShadowRadiusTypes | int):
        """
        There are two boxes (dmc.Paper() components).

        One represent header, other represent body.

        This parameter sets spacing between header
        and body box.
        """
        self.vertical_spacing = vertical_spacing

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_borders(self, with_borders: bool):
        """
        Purpose of this function is to put rectangle
        around dmc.Paper() component.

        It will put rectangle around both box like
        components - header and body component.
        """
        self.with_borders = with_borders

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def set_border_style(self, style: str):
        """
        Purpose of this function is to set style of
        borderline that are located on edges of dmc.Paper()
        component.

        """

        self.border_style = {
            "root": {
                # Color and width of border-line around
                # dmc.Paper() in which chart is located.
                "border": style,
                "borderTop": "none",
                # "borderBottom": "none"
            }
        }

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def get_card(self) -> dmc.SimpleGrid:
        """
        Purpose of this function is to return
        card component (header box + body box)
        to user.

        It will use configurations that were
        previously set up using configuration
        methods.
        """

        if self.header_content is not None:
            header_content = dmc.Paper(
                children=[self.header_content],
                id=self.header_id,
                withBorder=self.with_borders,
                h=40,
                radius=self.radius_header,
                shadow=self.shadow_header,
                styles={
                    "root": {
                        # Color and width of border-line around
                        # dmc.Paper() in which chart is located.
                        "border": "1px solid #777777",
                        "borderBottom": "none",
                        "backgroundColor": "#1a1e28",
                        # "marginBottom": "-1px"  # Slight overlap
                        # Purpose of these 3 lines is to artificially
                        # 'glue' upper and lower dmc.Paper() component,
                        # so that these two dmc.Paper() components look
                        # as single one.
                        "height": "120%",  # extend height slightly
                        "marginTop": "-10px",  # pull up to simulate extension
                        "marginBottom": "-10px",
                    }
                },
            )
        else:
            header_content = html.Div()

        return dmc.SimpleGrid(
            children=[
                self.hidden_content,
                header_content,
                dmc.Paper(
                    dmc.Box(
                        [
                            dmc.Stack(
                                pos="relative",
                                children=[
                                    dmc.LoadingOverlay(
                                        visible=False,
                                        id=self.chart_id + "loading-overlay",
                                        overlayProps={"radius": "xs", "blur": 2},
                                        zIndex=3,
                                    ),
                                    dcc.Graph(
                                        id=self.chart_id,
                                        # The idea of entire figure object here is
                                        # to create initial figure template so that
                                        # background color (while loading) is not
                                        # white, but dark.
                                        figure=go.Figure(
                                            data=[],  # Add your data here
                                            layout=go.Layout(
                                                plot_bgcolor="black",
                                                paper_bgcolor="black",
                                                font=dict(
                                                    color="black"
                                                ),  # Ensures text is readable on dark background
                                                xaxis=dict(
                                                    showgrid=False,  # Removes vertical grid lines
                                                    visible=False,  # Hides the x-axis
                                                ),
                                                yaxis=dict(
                                                    showgrid=False,  # Removes horizontal grid lines
                                                    visible=False,  # Hides the y-axis
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                            )
                        ]
                    ),
                    withBorder=self.with_borders,
                    radius=self.radius_body,
                    shadow=self.shadow_body,
                    styles=self.border_style,
                ),
            ],
            cols=1,
            verticalSpacing=self.vertical_spacing,
        )
