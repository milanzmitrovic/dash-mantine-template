"""

This is starting point of entire project.

It is actually main file of entire application.

"""

from .utils.CreateApp import create_app


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

    app.run()


if __name__ == "__main__":
    # This part is necessary so that
    # app can be run from IDE like
    # PyCharm.
    # Command: uv run dash-mantine-template
    # does NOT need it.
    main()
