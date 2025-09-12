"""

Purpose of this file is to organize
components that will be put on RIGHT
side of application view.

RIGHT side of page.

"""

import dash_mantine_components as dmc
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def aside_component() -> dmc.AppShellAside:
    """
    Purpose of this function is to
    create UI component that will
    be shown on RIGHT side of entire
    app's view.

    :return dmc.AppShellAside component
    """
    return dmc.AppShellAside(["123"])
