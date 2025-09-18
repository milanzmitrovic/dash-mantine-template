"""
Purpose of this file is to help with
loading .env file at the beginning of
project initialization.

Otherwise, env vars could be used
before they are loaded.
"""

from dotenv import load_dotenv

load_dotenv()
