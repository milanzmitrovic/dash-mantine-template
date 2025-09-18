"""
Purpose of this file is to organize
tests for database connections.
"""

from unittest.mock import MagicMock, patch

import pytest
from sqlalchemy.engine.cursor import CursorResult

from dash_mantine_template.utils.database.SqlAlchemy import SqlConnector


@pytest.fixture
def sql_connector():
    """
    x
    """
    return SqlConnector(
        postgres_user="user",
        postgres_password="pass",
        postgres_host="localhost",
        postgres_port=5432,
        postgres_db="test_db",
    )


def _mock_connection(mock_connect):
    """Helper to return a mock connection object with a CursorResult-like execute."""
    mock_conn = MagicMock()
    # Ensure execute returns something Pydantic accepts
    mock_cursor_result = MagicMock(spec=CursorResult)
    mock_conn.execute.return_value = mock_cursor_result
    mock_connect.return_value.__enter__.return_value = mock_conn
    return mock_conn, mock_cursor_result


def test_ddl_statement(sql_connector):
    with patch.object(sql_connector.engine, "connect") as mock_connect:
        mock_conn, _ = _mock_connection(mock_connect)

        result = sql_connector.ddl_statement("CREATE TABLE test (id INT)")

        mock_conn.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        assert isinstance(result, CursorResult)


def test_create_statement(sql_connector):
    with patch.object(sql_connector.engine, "connect") as mock_connect:
        mock_conn, _ = _mock_connection(mock_connect)

        result = sql_connector.create_statement(
            "INSERT INTO test (id) VALUES (:id)", {"id": 1}
        )

        mock_conn.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        assert isinstance(result, CursorResult)


def test_read_statement(sql_connector):
    with patch.object(sql_connector.engine, "connect") as mock_connect:
        mock_conn, _ = _mock_connection(mock_connect)

        result = sql_connector.read_statement(
            "SELECT * FROM test WHERE id=:id", {"id": 1}
        )

        mock_conn.execute.assert_called_once()
        mock_conn.commit.assert_not_called()
        assert isinstance(result, CursorResult)


def test_update_statement(sql_connector):
    with patch.object(sql_connector.engine, "connect") as mock_connect:
        mock_conn, _ = _mock_connection(mock_connect)

        result = sql_connector.update_statement(
            "UPDATE test SET name=:name WHERE id=:id",
            {"id": 1, "name": "Bob"},
        )

        mock_conn.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        assert isinstance(result, CursorResult)


def test_delete_statement(sql_connector):
    with patch.object(sql_connector.engine, "connect") as mock_connect:
        mock_conn, _ = _mock_connection(mock_connect)

        result = sql_connector.delete_statement(
            "DELETE FROM test WHERE id=:id", {"id": 1}
        )

        mock_conn.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        assert isinstance(result, CursorResult)
