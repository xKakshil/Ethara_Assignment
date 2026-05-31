from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.mixins import UUIDMixin
from app.models.mixins import TimestampMixin


class Order(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "orders"

    customer_id: Mapped[UUID] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    customer = relationship(
        "Customer"
    )

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )
    @property
    def customer_name(self):
       return self.customer.name