from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.exceptions import (
    DuplicateSkuError,
    ProductNotFoundError,
)

from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
)

from app.services.product_service import (
    ProductService,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    payload: ProductCreate,
    db: Session = Depends(get_db),
):
    service = ProductService(db)

    try:
        return service.add_product(payload)

    except DuplicateSkuError:
        raise HTTPException(
            status_code=400,
            detail="SKU already exists",
        )


@router.get(
    "",
    response_model=list[ProductResponse],
)
def list_products(
    db: Session = Depends(get_db),
):
    service = ProductService(db)

    return service.list_products()


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_product(
    product_id: UUID,
    db: Session = Depends(get_db),
):
    service = ProductService(db)

    return service.get_product(product_id)


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product(
    product_id: UUID,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
):
    service = ProductService(db)

    try:
        return service.update_product(
            product_id,
            payload,
        )

    except ProductNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    except DuplicateSkuError:
        raise HTTPException(
            status_code=400,
            detail="SKU already exists",
        )


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_product(
    product_id: UUID,
    db: Session = Depends(get_db),
):
    service = ProductService(db)

    try:
        service.remove_product(product_id)

    except ProductNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )