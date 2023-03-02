import logging
from filecmp import cmp
from pathlib import Path

import pytest

from OTVision.helpers.log import LOG_LEVEL_INTEGERS, VALID_LOG_LEVELS, log

from .log_maker import LogMaker


class WrongNumberOfFilesFoundError(Exception):
    "Too few or too many log files have been created during this test run"
    pass


class TestLog:
    log_maker: LogMaker = LogMaker()

    log.formatter = logging.Formatter(
        "%(levelname)s (%(filename)s::%(funcName)s" "::%(lineno)d): %(message)s"
    )

    @pytest.mark.parametrize("level", VALID_LOG_LEVELS)
    def test_logger_logs_correct_message_for_level_in_other_file(
        self, level: str, caplog: pytest.LogCaptureFixture
    ) -> None:
        # Make log
        self.log_maker.log_str_level(level=level)

        # Check if log message including level is in log capture
        assert f"This is a {level} log" in caplog.text

    def test_logger_logs_caught_exception_properly(
        self, caplog: pytest.LogCaptureFixture
    ) -> None:
        # Create log message
        log_msg = "This is a log message for a custom error"

        # Make log
        self.log_maker.raise_error_and_log(log_msg)

        # Check if log message, error message and traceback are correct
        assert log_msg in caplog.text
        assert "MyCustomError" in caplog.text

    @pytest.mark.parametrize("logger_level", VALID_LOG_LEVELS)
    @pytest.mark.parametrize("log_level", VALID_LOG_LEVELS)
    def test_console_handler_logs_correct_message_only_above_his_level(
        self, logger_level: str, log_level: str, capsys: pytest.CaptureFixture
    ) -> None:
        # Get levels
        log_level_int = LOG_LEVEL_INTEGERS[log_level]
        logger_level_int = LOG_LEVEL_INTEGERS[logger_level]

        # Add console handler
        log.add_console_handler(level=logger_level)

        # Make log
        self.log_maker.log_int_level(level=log_level)

        # Read and return console output
        stdout, stderr = capsys.readouterr()

        # Check if log message including level is in console output
        if log_level_int >= logger_level_int:
            assert (
                f"This is a numeric level {log_level_int} a.k.a. {log_level} log"
                in stdout
            )
        else:
            assert stdout == ""

    def test_file_handler_logs_correct_content_to_file(
        self,
        test_data_tmp_dir: Path,
        test_data_dir: Path,
    ) -> None:
        # Add file handler
        log_dir = test_data_tmp_dir / "log"
        log.add_file_handler(level="DEBUG", log_dir=log_dir)

        # Make logs
        for level in VALID_LOG_LEVELS:
            self.log_maker.log_str_level(level=level)

        # Get reference log file name
        ref_log_file = test_data_dir / "log" / "_otvision_logs" / "test.log"

        # Get test log file name
        test_log_files = list((log_dir / "_otvision_logs").glob("*log"))
        if len(test_log_files) != 1:
            raise WrongNumberOfFilesFoundError
        test_log_file = test_log_files[0]

        # Compare test and reference log files
        assert cmp(ref_log_file, test_log_file)
