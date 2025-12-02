import contextvars
import types

request_global = contextvars.ContextVar(
    "request_global", default=types.SimpleNamespace()
)


def get_request_context():
    return request_global.get()
