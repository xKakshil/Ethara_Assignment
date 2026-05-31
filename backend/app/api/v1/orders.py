from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.exceptions import (
    CustomerNotFoundError,
    ProductNotFoundError,
    OrderNotFoundError,
    InsufficientStockError,
)

from app.schemas.order import (
    OrderCreate,
    OrderResponse,
)

from app.services.order_service import (
    OrderService,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    payload: OrderCreate,
    db: Session = Depends(get_db),
):
    service = OrderService(db)

    return service.create_order(payload)


@router.get(
    "",
    response_model=list[OrderResponse],
)
def list_orders(
    db: Session = Depends(get_db),
):
    service = OrderService(db)

    return service.list_orders()


@router.get(
    "/{order_id}",
    response_model=OrderResponse,
)
def get_order(
    order_id: UUID,
    db: Session = Depends(get_db),
):
    service = OrderService(db)

    try:
        return service.get_order(order_id)

    except OrderNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_order(
    order_id: UUID,
    db: Session = Depends(get_db),
):
    service = OrderService(db)

    try:
        service.remove_order(order_id)

    except OrderNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )