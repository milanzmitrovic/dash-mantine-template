from enum import Enum

import dash_mantine_components as dmc
from dash import Input, Output, callback, clientside_callback
from dash_iconify import DashIconify
from pydantic import ConfigDict, validate_call

from dash_mantine_template.component_ids.containers.DummyOutputs import (
    OnThemeChange,
    ThemeClientsideCallback,
)
from dash_mantine_template.component_ids.miscellaneous.ThemeSwitch import (
    ThemeSwitchComponent,
)


def theme_switch():
    return dmc.Switch(
        offLabel=DashIconify(
            icon="radix-icons:moon",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][8],
        ),
        onLabel=DashIconify(
            icon="radix-icons:sun",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][6],
        ),
        id=ThemeSwitchComponent.id.value,
        persistence=True,
        color="grey",
    )


clientside_callback(
    """
    (switchOn) => {

        // Main logic is implemented here.
        // Setting value dark/light to 
        // attribute data-mantine-color-scheme 
        // of HTML scheme.
        document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'light' : 'dark');

        // This is just due to sth must be returned 
        // by Dash callback as per design.
       return window.dash_clientside.no_update
    }
    """,
    Output(ThemeClientsideCallback.id.value, ThemeClientsideCallback.property.value),
    Input(ThemeSwitchComponent.id.value, ThemeSwitchComponent.property.value),
)


class Theme(Enum):
    DARK = False
    LIGHT = True


# This we can use for dynamically
# changing charts based on background
# color that user chose.
@callback(
    Output(OnThemeChange.id.value, OnThemeChange.property.value),
    Input(ThemeSwitchComponent.id.value, ThemeSwitchComponent.property.value),
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def on_theme_change(input_: Theme):
    """
    false --> light
    true --> dark

    """
    print(input_)
    print(type(input_))
    return f"[{input_}]"
