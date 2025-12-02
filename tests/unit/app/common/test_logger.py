from types import SimpleNamespace

import app.common.context_variables as global_vars
from app.common.logger import JSONFormatter, configure_logger, logger


class TestLogger:
    def test_logger_json_formatter_format(self):
        initial_g = SimpleNamespace()
        initial_g.request_id = "test"
        initial_g.origin = "www.hotes.cloudbeds.com"
        initial_g.x_amzn_trace_id = "123456789"
        initial_g.x_property_id = "79"
        initial_g.user_id = "123"
        initial_g.user_email = "asd@asd.asd"
        global_vars.request_global.set(initial_g)
        request_content = global_vars.get_request_context()
        json = JSONFormatter().json_record(
            message=None,
            extra=dict(time="custotime", x_amzn_trace_id="544545"),
            record=SimpleNamespace(
                exc_info=None, filename="as.json", funcName="a", levelname="WARNING"
            ),
        )
        assert json["x-amzn-trace-id"] == request_content.x_amzn_trace_id
        assert json["origin"] == request_content.origin

    def test_logger_json_formatter_format_no_user_data(self):
        initial_g = SimpleNamespace()
        initial_g.request_id = "test"
        initial_g.origin = "www.hotes.cloudbeds.com"
        initial_g.x_amzn_trace_id = "123456789"
        initial_g.x_property_id = "79"
        global_vars.request_global.set(initial_g)
        request_content = global_vars.get_request_context()
        json = JSONFormatter().json_record(
            message=None,
            extra=dict(time="custotime", x_amzn_trace_id="544545"),
            record=SimpleNamespace(
                exc_info=None, filename="as.json", funcName="a", levelname="WARNING"
            ),
        )
        assert json["x-amzn-trace-id"] == request_content.x_amzn_trace_id
        assert json["origin"] == request_content.origin

    def test_configure_logger(self):
        # Try out the logger at each level
        # (more complicated IO can be done to test the format or message if needed)
        configure_logger()
        logger.debug("Testing logger debug")
        logger.info("Testing logger info")
        logger.warning("Testing logger warning")
        logger.error("Testing logger error", exc_info="Mock Exception Info")

    def test_to_json(self):
        assert "{}" == JSONFormatter().to_json(SimpleNamespace(test=123))
