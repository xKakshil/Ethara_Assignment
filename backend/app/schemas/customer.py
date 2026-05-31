from uuid import UUID
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field


class CustomerCreate(BaseModel):
    full_name: str = Field(
        min_length=2,
        max_length=255
    )

    email: EmailStr

    phone: str = Field(
        min_length=8,
        max_length=20
    )


class CustomerResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID
    full_name: str
    email: EmailStr
    phone: str
    created_at: datetime
    updated_at: datetime