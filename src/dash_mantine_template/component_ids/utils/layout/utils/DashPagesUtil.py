"""
Purpose of this file is to organize
logic related to IDs and properties
of TAB component.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Tabs__ID:
    """
    ID of TAB component.
    """

    id: str = "tabs-id"


@dataclass(frozen=True)
class Tabs__Property:
    """
    Property of TAB component.
    """

    value: str = "value"


tabs__id = Tabs__ID()

tabs__property = Tabs__Property()
