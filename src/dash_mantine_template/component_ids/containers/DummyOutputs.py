"""
Purpose of this file is to
organize logic related with
IDs of components that are
holding dummy elements.

Dummy components are elements
that are necessary only in
order to keep proper input/output
logic related with Dash callback
components.

Some components does not need
any output element, but Dash
by its design requires that each
callback has output element.

So, we will create dummy
output component for that
purpose.

"""

from enum import Enum


class ThemeClientsideCallback(Enum):
    id: str = "fdfedf"
    property: str = "children"


class OnThemeChange(Enum):
    id: str = "cdcdc"
    property: str = "children"
