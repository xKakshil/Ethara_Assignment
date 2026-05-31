from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.exceptions import (
    CustomerNotFoundError,
    DuplicateEmailError,
)

from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
)

from app.services.customer_service import (
    CustomerService,
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_customer(
    payload: CustomerCreate,
    db: Session = Depends(get_db),
):
    service = CustomerService(db)

    return service.add_customer(payload)


@router.get(
    "",
    response_model=list[CustomerResponse],
)
def list_customers(
    db: Session = Depends(get_db),
):
    service = CustomerService(db)

    return service.list_customers()


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def get_customer(
    customer_id: UUID,
    db: Session = Depends(get_db),
):
    service = CustomerService(db)

    try:
        return service.get_customer(customer_id)

    except CustomerNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )


@router.delete(
    "/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_customer(
    customer_id: UUID,
    db: Session = Depends(get_db),
):
    service = CustomerService(db)

    try:
        service.remove_customer(customer_id)

    except CustomerNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )