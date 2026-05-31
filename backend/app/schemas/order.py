from decimal import Decimal
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class OrderItemCreate(BaseModel):
    product_id: UUID

    quantity: int = Field(
        gt=0
    )


class OrderCreate(BaseModel):
    customer_id: UUID

    items: list[OrderItemCreate] = Field(
        min_length=1
    )


class OrderItemResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    product_id: UUID
    product_name: str

    quantity: int
    unit_price: Decimal
    subtotal: Decimal

class OrderResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    customer_id: UUID
    customer_name: str

    total_amount: Decimal

    items: list[OrderItemResponse]

    created_at: datetime
    updated_at: datetime