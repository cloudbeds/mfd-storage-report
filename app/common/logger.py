import json
import logging
import sys
from datetime import datetime

from app.common.context_variables import get_request_context
from app.config import settings

LOGGER = "python-restapi-template"

BUILTIN_ATTRS = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
}


class JSONFormatter(logging.Formatter):
    def __init__(self, date_format: str = "%Y-%m-%dT%H:%M:%S"):
        self.datefmt = date_format

    def format(self, record):
        message = record.getMessage()
        extra = self.extra_from_record(record)
        json_record = self.json_record(message, extra, record)
        return self.to_json(json_record)

    def to_json(self, record):
        """Converts record dict to a JSON string."""
        try:
            return json.dumps(record)
        except (TypeError, ValueError, OverflowError):
            return "{}"

    def extra_from_record(self, record):
        """Returns `extra` dict you passed to logger.

        The `extra` keyword argument is used to populate the `__dict__` of
        the `LogRecord`.

        """
        return {
            attr_name: record.__dict__[attr_name]
            for attr_name in record.__dict__
            if attr_name not in BUILTIN_ATTRS
        }

    def json_record(self, message, extra, record):
        """Prepares a JSON payload which will be logged.

        Override this method to change JSON log format.

        If is needed to use more python built in args please define it below

        :param message: Log message, e.g., `logger.info(msg='Create report')`.
        :param extra: Dictionary that was passed as `extra` param
            `logger.info('Creating Report, extra={'report_id': '52d6ce'})`.
        :param record: `LogRecord` we got from `JSONFormatter.format()`.
        :return: Dictionary which will be passed to JSON lib.

        """
        context_variables = get_request_context()

        extra["filename"] = record.filename
        extra["function"] = record.funcName
        extra["level"] = record.levelname
        extra["origin"] = (
            context_variables.origin if hasattr(context_variables, "origin") else "-"
        )
        extra["request_id"] = (
            context_variables.request_id
            if hasattr(context_variables, "request_id")
            else "-"
        )

        # Add the expected key for amzn trace id
        extra["x-amzn-trace-id"] = (
            context_variables.x_amzn_trace_id
            if hasattr(context_variables, "x_amzn_trace_id")
            else "-"
        )

        extra["property_id"] = (
            context_variables.property_id
            if hasattr(context_variables, "property_id")
            else "-"
        )

        if hasattr(context_variables, "user_id"):
            extra["user_id"] = context_variables.user_id

        if hasattr(context_variables, "user_email"):
            extra["user_email"] = context_variables.user_email

        if hasattr(context_variables, "endpoint"):
            extra["endpoint"] = context_variables.endpoint

        if hasattr(record, "stack_info"):
            extra["stack_info"] = record.stack_info

        extra["message"] = message

        if "time" not in extra:
            extra["time"] = datetime.utcnow().strftime(self.datefmt)

        if record.exc_info:
            extra["exc_info"] = self.formatException(record.exc_info)

        return extra


def configure_logger():
    logging_stream_handler = logging.StreamHandler()
    logging_stream_handler.setStream(stream=sys.stdout)
    logging_stream_handler.setFormatter(JSONFormatter())

    logger = logging.getLogger(LOGGER)
    logger.setLevel(settings.LOG_LEVEL)
    logger.addHandler(logging_stream_handler)


logger = logging.getLogger(LOGGER)
