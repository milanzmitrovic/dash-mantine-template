""" """

import logging
from logging.handlers import TimedRotatingFileHandler


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

    def error(self, message: str):
        """

        :param message:
        :return:
        """
        self.logger.error(msg=message)

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


logger = Logger(logger_name="dmt", logger_location="temp/logs/app.log")
