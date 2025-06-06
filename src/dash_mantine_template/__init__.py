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
    app.run()


if __name__ == "__main__":
    main()
