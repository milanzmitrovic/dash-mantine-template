"""
Purpose of this file is to
organize tests for Logging
class.

There is test for each log
method.
"""

import os
import tempfile
import time

from dash_mantine_template.utils.logging.Logger import (
    Logger,
)


def test__logger__info():
    # Create a temporary log file
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        log_path = temp_log.name

    try:
        # Initialize the logger with temp file
        logger = Logger(logger_name="test_logger__info", logger_location=log_path)

        # Write a log line
        logger.info("test log message")

        # Sleep shortly to ensure file write completes (esp. for rotating handlers)
        time.sleep(0.1)

        # Read the log file and verify the message
        with open(log_path, "r") as f:
            content = f.read()

            assert "test log message" in content
            assert "INFO" in content

    finally:
        # Clean up temp file
        os.remove(log_path)


def test__logger__warning():
    # Create a temporary log file
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        log_path = temp_log.name

    try:
        # Initialize the logger with temp file
        logger = Logger(logger_name="test_logger__warning", logger_location=log_path)

        # Write a log line
        logger.warning("test log message")

        # Sleep shortly to ensure file write completes (esp. for rotating handlers)
        time.sleep(0.1)

        # Read the log file and verify the message
        with open(log_path, "r") as f:
            content = f.read()

            assert "test log message" in content
            assert "WARNING" in content

    finally:
        # Clean up temp file
        os.remove(log_path)


def test__logger__error():
    # Create a temporary log file
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        log_path = temp_log.name

    try:
        # Initialize the logger with temp file
        logger = Logger(logger_name="test_logger__error", logger_location=log_path)

        # Write a log line
        logger.error("test log message")

        # Sleep shortly to ensure file write completes (esp. for rotating handlers)
        time.sleep(0.1)

        # Read the log file and verify the message
        with open(log_path, "r") as f:
            content = f.read()

            assert "test log message" in content
            assert "ERROR" in content

    finally:
        # Clean up temp file
        os.remove(log_path)


def test__logger__critical():
    # Create a temporary log file
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        log_path = temp_log.name

    try:
        # Initialize the logger with temp file
        logger = Logger(logger_name="test_logger__critical", logger_location=log_path)

        # Write a log line
        logger.critical("test log message")

        # Sleep shortly to ensure file write completes (esp. for rotating handlers)
        time.sleep(0.1)

        # Read the log file and verify the message
        with open(log_path, "r") as f:
            content = f.read()

            assert "test log message" in content
            assert "CRITICAL" in content

    finally:
        # Clean up temp file
        os.remove(log_path)


def test__logger__debug():
    # Create a temporary log file
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        log_path = temp_log.name

    try:
        # Initialize the logger with temp file
        logger = Logger(logger_name="test_logger__debug", logger_location=log_path)

        # Write a log line
        logger.debug("test log message")

        # Sleep shortly to ensure file write completes (esp. for rotating handlers)
        time.sleep(0.1)

        # Read the log file and verify the message
        with open(log_path, "r") as f:
            content = f.read()

            assert "test log message" in content
            assert "DEBUG" in content

    finally:
        # Clean up temp file
        os.remove(log_path)
