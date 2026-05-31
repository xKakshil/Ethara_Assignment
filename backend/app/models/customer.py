from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base
from app.models.mixins import UUIDMixin
from app.models.mixins import TimestampMixin


class Customer(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "customers"

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )