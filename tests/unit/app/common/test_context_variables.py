import types

import app.common.context_variables as global_vars


class TestGlobalVars:
    def test_get_request_content(self):
        initial_g = types.SimpleNamespace()
        initial_g.request_id = "test"
        initial_g.origin = "www.hotes.cloudbeds.com"
        initial_g.x_amzn_trace_id = "123456789"
        initial_g.x_property_id = "79"
        global_vars.request_global.set(initial_g)
        request_content = global_vars.get_request_context()
        assert request_content.request_id == initial_g.request_id
        assert request_content.x_amzn_trace_id == initial_g.x_amzn_trace_id
        assert request_content.x_amzn_trace_id == initial_g.x_amzn_trace_id
        assert request_content.x_property_id == initial_g.x_property_id
