"""
Purpose of this file is to organize logic
related to IDs and properties of select
component.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SelectComponent__ID:
    """ """

    id: str = "analytics-input"


@dataclass(frozen=True)
class SelectComponent__Property:
    """ """

    value: str = "value"


# --- --- --- #


@dataclass(frozen=True)
class OutputComponent__ID:
    """ """

    id: str = "analytics-output"


@dataclass(frozen=True)
class OutputComponent__Property:
    """ """

    children: str = "children"


select_component__id = SelectComponent__ID()

select_component__property = SelectComponent__Property()

# --- --- --- #

output_component__id = OutputComponent__ID()

output_component__property = OutputComponent__Property()
