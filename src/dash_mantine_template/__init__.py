"""

This is starting point of entire project.

It is actually main file of entire application.

"""

# Make sure that config import is always written
# as first importing file. Why? We should be sure
# that env variables are loaded as first step after
# app is run.
# We need cc alias here so that we can use custom components
# using fancy importing i.e. so that we can import it from
# project name.
import dash_mantine_template.utils.global_components as gc # noqa: F401

from dash_mantine_template.config import *  # noqa: F403
from dash_mantine_template.context import app_context
from dash_mantine_template.utils.CreateApp import create_app


def main():
    """
    Purpose of this function is to
    start entire application.
    """
    app = create_app()

    # Open file that is holding initial
    # html of page.
    # It is loaded on page refresh in
    # browser for less than 1 second.
    with open(
        "src/dash_mantine_template/components/miscellaneous/InitialTheme.html",
        "r",
        encoding="utf-8",
    ) as file:
        html_string = file.read()

    # Add html that should be loaded
    # on initial page refresh.
    app.index_string = html_string

    app.run(
        port=app_context.env_vars.app_port,
        host="0.0.0.0",
        debug=app_context.env_vars.debug,
    )


if __name__ == "__main__":
    # This part is necessary so that
    # app can be run from IDE like
    # PyCharm.
    # Command: uv run dash-mantine-template
    # does NOT need it.
    main()
