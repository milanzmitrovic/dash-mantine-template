"""
Purpose of this file is to
organize logic for header
component of Dash app.

Top of the page.

"""

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call

from .....components.miscellaneous.ThemeSwitch import theme_switch


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def header_component() -> dmc.AppShellHeader:
    """
    Purpose of this function is to
    create component that will be
    on top of page view.

    It will be component from
    Mantine library.

    :return dmc.AppShellHeader component.
    """
    return dmc.AppShellHeader(
        children=[
            dmc.Flex(
                align="center",
                justify="space-between",
                gap="md",
                style={"padding": "10px", "backgroundColor": "#f0f0f0"},
                children=[
                    # Far left element
                    dmc.Text(
                        "Left Component    ", style={"color": "var(--universal-color)"}
                    ),
                    # Center group (wrapped in another Flex with margin auto)
                    dmc.Flex(
                        gap="md",
                        justify="center",
                        align="center",
                        style={"margin": "0 auto"},
                        children=[
                            dmc.Text(
                                "Dash Mantine Template - Header component",
                                style={"color": "var(--universal-color)"},
                            ),
                        ],
                    ),
                    # Far right element
                    theme_switch(),
                ],
            ),
        ]
    )
