from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.v1.products import (
    router as product_router,
)
from app.api.v1.customers import (
    router as customer_router,
)
from app.api.v1.orders import (
    router as order_router,
)
from app.api.v1.dashboard import (
    router as dashboard_router,
)

from app.core.exceptions import (
    ProductNotFoundError,
    CustomerNotFoundError,
    OrderNotFoundError,
    DuplicateSkuError,
    DuplicateEmailError,
    InsufficientStockError,
)

from app.core.exception_handlers import (
    product_not_found_handler,
    customer_not_found_handler,
    order_not_found_handler,
    duplicate_sku_handler,
    duplicate_email_handler,
    insufficient_stock_handler,
)

app = FastAPI(
    title="Inventory Management API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception Handlers

app.add_exception_handler(
    ProductNotFoundError,
    product_not_found_handler,
)

app.add_exception_handler(
    CustomerNotFoundError,
    customer_not_found_handler,
)

app.add_exception_handler(
    OrderNotFoundError,
    order_not_found_handler,
)

app.add_exception_handler(
    DuplicateSkuError,
    duplicate_sku_handler,
)

app.add_exception_handler(
    DuplicateEmailError,
    duplicate_email_handler,
)

app.add_exception_handler(
    InsufficientStockError,
    insufficient_stock_handler,
)


# Routers

app.include_router(
    product_router,
    prefix="/api/v1",
)

app.include_router(
    customer_router,
    prefix="/api/v1",
)

app.include_router(
    order_router,
    prefix="/api/v1",
)

app.include_router(
    dashboard_router,
    prefix="/api/v1",
)


@app.get(
    "/",
    tags=["Health"],
)
def health_check():
    return {
        "status": "healthy",
        "service": "inventory-api",
        "version": "1.0.0",
    }
