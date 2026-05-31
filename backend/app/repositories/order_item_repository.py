from sqlalchemy.orm import Session

from app.models.order_item import OrderItem


class OrderItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        order_item: OrderItem,
    ):
        self.db.add(order_item)

        return order_item