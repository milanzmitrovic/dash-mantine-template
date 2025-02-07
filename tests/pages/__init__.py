"""
Purpose of this folder it to organize
tests related to Dash pages logic.

In other words, let's check that each
page is present and make sure layout
is properly organized.


Unfortunatelly, there is issue with
dash.register_page() function. In other
words, this functio is called at
import time, so it is not possible
to patch that function.

Alternative logic for testing
layout in Dash pages should be
developed.
"""
