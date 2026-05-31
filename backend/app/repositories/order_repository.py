from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, order_id: UUID):
        stmt = select(Order).where(
            Order.id == order_id
        )

        return self.db.scalar(stmt)

    def list_all(self):
        stmt = select(Order).order_by(
            Order.created_at.desc()
        )

        return list(
            self.db.scalars(stmt).all()
        )

    def create(self, order: Order):
        self.db.add(order)

        return order

    def delete(self, order: Order):
        self.db.delete(order)