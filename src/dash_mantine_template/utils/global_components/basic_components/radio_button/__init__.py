"""
Purpose of this file is to help with
organization of imports.

Now, all namespaces imported in this
file will available in entire app via
gc.number_input...
"""

from .Component import component  # noqa: F401
from .Input import input_, input_dummy  # noqa: F401
from .Output import output  # noqa: F401
