from decimal import Decimal
from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class ProductCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=255
    )

    sku: str = Field(
        min_length=2,
        max_length=100
    )

    description: Optional[str] = None

    price: Decimal = Field(
        gt=0
    )

    stock_quantity: int = Field(
        ge=0
    )


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = Field(
        default=None,
        gt=0
    )
    stock_quantity: Optional[int] = Field(
        default=None,
        ge=0
    )


class ProductResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID
    name: str
    sku: str
    description: Optional[str]
    price: Decimal
    stock_quantity: int
    created_at: datetime
    updated_at: datetime