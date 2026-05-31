from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.customer import Customer
from app.models.order import Order


class DashboardRepository:
    def __init__(self, db: Session):
        self.db = db

    def total_products(self):
        stmt = select(
            func.count(Product.id)
        )

        return self.db.scalar(stmt) or 0

    def total_customers(self):
        stmt = select(
            func.count(Customer.id)
        )

        return self.db.scalar(stmt) or 0

    def total_orders(self):
        stmt = select(
            func.count(Order.id)
        )

        return self.db.scalar(stmt) or 0

    def low_stock_products(
        self,
        threshold: int = 5,
    ):
        stmt = (
            select(Product)
            .where(
                Product.stock_quantity <= threshold
            )
            .order_by(
                Product.stock_quantity.asc()
            )
        )

        return list(
            self.db.scalars(stmt).all()
        )