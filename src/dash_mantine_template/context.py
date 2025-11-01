# context.py
from dataclasses import dataclass

from .config import EnvContext


@dataclass
class AppContext:
    """
    1
    """

    env_vars: EnvContext
    db: str
    logger: str

    @classmethod
    def create(cls):
        """
        2
        """
        db = ""
        logger = ""
        env_vars = EnvContext()  # loads from env/.env
        return cls(env_vars=env_vars, db=db, logger=logger)


app_context = AppContext.create()
