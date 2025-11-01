"""
Purpose of this file is to organize
logic related to logging functionality
of application.

There is Logging class and logger
object instantiated in this file.

Object logger should be used throughout
application for logging. It has all
necessary methods for performing
logs.

"""

import logging
import sys
import threading
from logging.handlers import TimedRotatingFileHandler

from dash_mantine_template.context import app_context


class Logger:
    """
    Purpose of this class is to create
    interface for logging.

    All necessary methods should be
    present here:
        - info()
        - warning()
        - error()
        - critical()
    """

    def __init__(self, logger_name: str, logger_location: str):
        """

        Location on which .log file should be
        created when app is started first time,
        should be created.

        Logger can only create .log file (if not
        already exists).
        Loffer cannot create folder in which .log
        file should be stored.

        :param logger_name: Name of logger (will be
                            written in .log file).

        :param logger_location: Name of .log file.
        """

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)  # Set to lowest level to capture all logs

        # Prevent adding multiple handlers in case of re-instantiation
        if not self.logger.handlers:
            handler = TimedRotatingFileHandler(
                filename=logger_location,
                # New log every day at midnight.
                when="midnight",
                # Keep logs for previous 7 days.
                backupCount=7,
                encoding="utf-8",
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

            # Capture uncaught exceptions
            sys.excepthook = self.handle_exception

            # Capture thread exceptions (Python 3.8+)
            if hasattr(threading, "excepthook"):
                threading.excepthook = self.handle_thread_exception

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        """Global handler for uncaught exceptions in the main thread."""
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        self.logger.error(
            "Uncaught exception",
            exc_info=(exc_type, exc_value, exc_traceback),
        )

    def handle_thread_exception(self, args):
        """Global handler for uncaught exceptions in threads."""
        self.logger.error(
            "Uncaught thread exception",
            exc_info=(args.exc_type, args.exc_value, args.exc_traceback),
        )

    def info(self, message: str):
        """

        :param message:
        :return:
        """
        self.logger.info(msg=message)

    def warning(self, message: str):
        """

        :param message:
        :return:
        """
        self.logger.warning(msg=message)

    def error(self, message: str, exc_info: bool):
        """

        :param message:
        :param exc_info:
        :return:
        """
        self.logger.error(msg=message, exc_info=exc_info)

    def critical(self, message: str):
        """

        :param message:
        :return:
        """
        self.logger.critical(msg=message)

    def debug(self, message: str):
        """

        :param message:
        :return:
        """
        self.logger.debug(msg=message)


logger = Logger(
    logger_name="dmt", logger_location=app_context.env_vars.log_file_location
)
