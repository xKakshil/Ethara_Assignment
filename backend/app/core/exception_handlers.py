from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    ProductNotFoundError,
    CustomerNotFoundError,
    OrderNotFoundError,
    DuplicateSkuError,
    DuplicateEmailError,
    InsufficientStockError,
)


async def product_not_found_handler(
    request: Request,
    exc: ProductNotFoundError,
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": "Product not found"
        },
    )


async def customer_not_found_handler(
    request: Request,
    exc: CustomerNotFoundError,
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": "Customer not found"
        },
    )


async def order_not_found_handler(
    request: Request,
    exc: OrderNotFoundError,
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": "Order not found"
        },
    )


async def duplicate_sku_handler(
    request: Request,
    exc: DuplicateSkuError,
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "detail": "SKU already exists"
        },
    )


async def duplicate_email_handler(
    request: Request,
    exc: DuplicateEmailError,
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "detail": "Email already exists"
        },
    )


async def insufficient_stock_handler(
    request: Request,
    exc: InsufficientStockError,
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "detail": "Insufficient stock"
        },
    )