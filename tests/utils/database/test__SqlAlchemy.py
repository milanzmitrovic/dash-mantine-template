"""
Purpose of this file is to organize
tests for database connections.
"""

import pytest

from dash_mantine_template.utils.Database.SqlAlchemy import (
    SqlConnector,  # adjust this import to your actual file
)


@pytest.fixture
def connector():
    """
    PyTest fixture connection.
    """

    # Use in-memory SQLite DB
    return SqlConnector("sqlite+pysqlite:///:memory:")


def test__ddl_statement_creates_table(connector):
    """
    Purpose of this function is to
    test possibility to execute DDL
    type of SQL query.

    """

    ddl_query = """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """
    connector.ddl_statement(ddl_query)

    # Query sqlite_master to check if 'users' table exists
    check_table_query = """
    SELECT name FROM sqlite_master WHERE type='table' AND name='users';
    """
    result = connector.read_statement(check_table_query, parameters=None)
    row = result.mappings().fetchone()

    assert row is not None, "Table 'users' should be created"
    assert row["name"] == "users"


def test__create_and_read_statement(connector):
    """
    Purpose of this function is to
    test methods for executing CREATE
    and READ types of SQL query.

    """
    connector.ddl_statement("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")

    insert_query = "INSERT INTO users (id, name) VALUES (:id, :name)"
    connector.create_statement(insert_query, {"id": 1, "name": "Alice"})

    select_query = "SELECT * FROM users WHERE id=:id"
    result = connector.read_statement(select_query, {"id": 1})
    row = result.mappings().fetchone()
    assert row["id"] == 1
    assert row["name"] == "Alice"


def test__update_statement(connector):
    """
    Purpose of this function is to
    execute test for UPDATE method.
    """
    connector.ddl_statement("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    connector.create_statement(
        "INSERT INTO users (id, name) VALUES (:id, :name)", {"id": 1, "name": "Alice"}
    )

    update_query = "UPDATE users SET name=:name WHERE id=:id"
    result = connector.update_statement(update_query, {"id": 1, "name": "Bob"})
    assert result.rowcount == 1

    select = connector.read_statement("SELECT name FROM users WHERE id=:id", {"id": 1})
    row = select.mappings().fetchone()
    assert row["name"] == "Bob"


def test__delete_statement(connector):
    """
    Purpose of this function is to check
    if DELETE type of SQL query can be
    executed properly.
    """
    connector.ddl_statement("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    connector.create_statement(
        "INSERT INTO users (id, name) VALUES (:id, :name)", {"id": 1, "name": "Alice"}
    )

    delete_query = "DELETE FROM users WHERE id=:id"
    result = connector.delete_statement(delete_query, {"id": 1})
    assert result.rowcount == 1

    result = connector.read_statement("SELECT * FROM users WHERE id=:id", {"id": 1})
    assert result.fetchone() is None
