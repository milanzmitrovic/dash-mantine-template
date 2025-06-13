"""
Purpose of this file is to organize
logic for interactions with database.
"""

from typing import Dict, Optional

from pydantic import ConfigDict, validate_call
from sqlalchemy import create_engine, text
from sqlalchemy.engine.cursor import CursorResult


class SqlConnector:
    """
    Purpose of this class is to organize
    central logic for executing SQL queries.

    Following types of queries will be able
    to be executed:
        - DDL type of query
        - Create
        - Read
        - Update
        - Delete

    """

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def __init__(self, database_location: str):
        self.engine = create_engine(database_location)

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def ddl_statement(self, ddl_query: str) -> CursorResult:
        """
        Purpose of this method is to
        execute DDL type of query.


        :param ddl_query
        :return:
        """

        with self.engine.connect() as conn:
            result = conn.execute(text(ddl_query))
            conn.commit()

            return result

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def create_statement(
        self, sql_query: str, parameters: Optional[Dict]
    ) -> CursorResult:
        """
        Purpose of this method is to
        execute CREATE type of query.

        We can get number of rows that
        are written to table by this
        command:
            print(result.rowcount)


        :param sql_query:
        :param parameters:
        :return:
        """

        with self.engine.connect() as conn:
            result = conn.execute(
                statement=text(sql_query),
                parameters=parameters,
            )
            conn.commit()  # Required for insert/update/delete in SQLite

            return result

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def read_statement(
        self, sql_query: str, parameters: Optional[Dict]
    ) -> CursorResult:
        """
        Purpose of this method is to
        execute READ type of query.

        We can get data retrieved by
        looping through returned
        object:
            for i in result_r:
                print(i)

        We can get column of table
        to which data is written by
        this command:
            print(list(result_r.keys()))

        :param sql_query:
        :param parameters:
        :return:
        """

        # READ
        with self.engine.connect() as conn:
            result = conn.execute(
                statement=text(sql_query),
                parameters=parameters,
            )

            return result

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def update_statement(
        self, sql_query: str, parameters: Optional[Dict]
    ) -> CursorResult:
        """
        Purpose of this method is to
        execute UPDATE type of query.

        Using this command we can see
        how many rows are updated:
            print(result.rowcount)

        :param sql_query:
        :param parameters:
        :return:
        """
        with self.engine.connect() as conn:
            # Execute an UPDATE query
            result = conn.execute(
                statement=text(sql_query),
                parameters=parameters,
            )
            conn.commit()  # Required for changes in SQLite

            return result

    @validate_call(
        config=ConfigDict(arbitrary_types_allowed=True), validate_return=True
    )
    def delete_statement(
        self, sql_query: str, parameters: Optional[Dict]
    ) -> CursorResult:
        """
        Purpose of this method is to
        execute DELETE type of query.

        We can see how many rows were
        deleted by this command:
            print(result.rowcount)

        :param sql_query:
        :param parameters:
        :return:
        """
        with self.engine.connect() as conn:
            # Execute a DELETE query
            result = conn.execute(
                statement=text(sql_query),
                parameters=parameters,
            )
            conn.commit()  # Required for changes in SQLite

            return result


sql_connector = SqlConnector(
    database_location="sqlite:///./temp/sqlite_database/example.db"
)
