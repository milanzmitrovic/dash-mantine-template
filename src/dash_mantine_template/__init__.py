"""

This is starting point of entire project.

It is actually main file of entire application.

"""

from dash_mantine_template.utils.CreateApp import create_app


def main():
    """
    Purpose of this function is to
    start entire application.
    """
    app = create_app()

    # Open file that is holding initial
    # html of page.
    # It is loaded on page refresh.
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
    main()
