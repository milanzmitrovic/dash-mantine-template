"""
1
"""

from typing import List, TypedDict

from dash_mantine_template import gc


class SegmentedControlOutput(TypedDict):
    """
    1
    """

    data: List[str] | List[gc.segmented_control.DataDict]
    value: str
