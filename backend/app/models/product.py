from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import Integer
from sqlalchemy import Text
from typing import Optional
from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint
from decimal import Decimal

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base
from app.models.mixins import UUIDMixin
from app.models.mixins import TimestampMixin


class Product(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "products"
    __table_args__ = (
    CheckConstraint(
        "price > 0",
        name="check_product_price_positive"
    ),
    CheckConstraint(
        "stock_quantity >= 0",
        name="check_stock_non_negative"
    ),
)

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    sku: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    stock_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )
    order_items = relationship(
    "OrderItem",
    back_populates="product",
    cascade="all, delete-orphan"
)