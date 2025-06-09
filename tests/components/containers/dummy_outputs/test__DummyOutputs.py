"""
Purpose of this file is to
organize tests related to
component that is holding
dummy output elements.
"""

from dash import html

from dash_mantine_template.components.containers.dummy_outputs.DummyOutputs import (
    dummy_outputs,
)


def test__dummy_outputs():
    assert isinstance(dummy_outputs(), html.Div)
