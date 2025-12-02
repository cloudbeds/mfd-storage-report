import uuid
from types import SimpleNamespace

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import app.common.context_variables as global_vars
from app.modules.client.router import router as client_router
from app.modules.invoice.router import router as invoice_router
from app.modules.product.router import router as product_router

app = FastAPI(
    title="Fast API Rest API Template",
    description="Python Rest API Template.",
    docs_url="/docs",
    openapi_url="/docs/openapi.json",
)


# Initial Request Vars
@app.middleware("http")
async def init_requestvars(request: Request, call_next):
    # Customize that SimpleNamespace with whatever you need
    initial_g = SimpleNamespace()
    initial_g.request_id = str(uuid.uuid4())
    global_vars.request_global.set(initial_g)
    response = await call_next(request)
    return response


# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=("*",),
    allow_headers=("*",),
    allow_credentials=True,
    max_age=3600,
)

# Routers
app.include_router(invoice_router)
app.include_router(client_router)
app.include_router(product_router)
