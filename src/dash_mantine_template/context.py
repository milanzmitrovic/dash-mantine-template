# context.py
from dataclasses import dataclass

from .config import EnvContext


@dataclass
class AppContext:
    """
    Class representing context of Dash app.

    """

    env_vars: EnvContext
    example_app_context_variable: str

    @classmethod
    def create(cls):
        """
        Create context.
        """
        example_app_context_variable = ""
        env_vars = EnvContext()  # loads from env/.env
        return cls(
            env_vars=env_vars, example_app_context_variable=example_app_context_variable
        )


app_context = AppContext.create()
