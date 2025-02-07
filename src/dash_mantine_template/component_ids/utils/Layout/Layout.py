"""
Purpose of this file is to organize
classes where IDs and properties of
url/location component will be stored.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LocationURL__ID:
    """
    ID of URL/Pathname component.
    """

    id: str = "app-url-location"


@dataclass(frozen=True)
class LocationURL__Property:
    """
    Property of URL/Pathname component.
    """

    pathname: str = "pathname"


location_url__id = LocationURL__ID()

location_url_property = LocationURL__Property()
