"""
Purpose of this file is to store dummy
output elements.

There are callbacks that do not need to
have outputs (clientside callback, component
that is just getting input from UI and not
returning anything, ...).

Here we will group all such components
in order to have them in one place.

"""

from dash import html

from dash_mantine_template.component_ids.containers.DummyOutputs import (
    OnThemeChange,
    ThemeClientsideCallback,
)


def dummy_outputs():
    return html.Div(
        [
            html.Div(id=ThemeClientsideCallback.id.value),
            html.Div(id=OnThemeChange.id.value),
        ]
    )
