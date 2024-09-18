"""Test main file functionality here."""


import polars as pl

from main import example_function


def test_example_function():
    """

    Initial test.

    Purpose is to make sure that testing framework works.

    :return:
    """
    assert isinstance(example_function(), pl.DataFrame)
