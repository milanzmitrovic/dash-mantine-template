"""
Purpose of this file is to organize layout component
of the app.
"""

import dash_mantine_components as dmc
from dash import dcc
from pydantic import ConfigDict, validate_call

from ...component_ids.utils.layout.Layout import location_url__id
from ...components.containers.dummy_outputs.DummyOutputs import (
    dummy_outputs,
)

from .utils.app_shell.AppShell import app_shell
from .utils.app_shell.Header import header_component
from .utils.app_shell.Main import main_component

# from .utils.app_shell.Aside import aside_component
# from .utils.app_shell.Navbar import navbar_component
from .utils.MantineProvider import mantine_provider


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def layout() -> dmc.MantineProvider:
    """
    Purpose of this component is to
    create entire layout of Dash app.

    It has:
        - Main component
        - Header component
        - Optionally, navbar component
        - Optionally, aside component

    Of course, everything lives inside
    Mantine provider.

    So, Mantine styles applies to each
    and every component in the app.

    :return MantineProvider object.
    """

    return mantine_provider(
        content=[
            dcc.Location(id=location_url__id.id),
            dummy_outputs(),
            app_shell(
                content=[
                    main_component(),
                    header_component(),
                    # navbar_component(),
                    # aside_component(),
                ]
            ),
        ]
    )
