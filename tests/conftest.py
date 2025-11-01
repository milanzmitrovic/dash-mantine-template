import os

# This is important so that we can know
# when AppContext is running as part of
# Dash app itself, and when it is running
# as part of PyTests.
os.environ["PYTEST_RUNNING"] = "true"
