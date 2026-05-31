from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id: UUID):
        stmt = select(Product).where(
            Product.id == product_id
        )

        return self.db.scalar(stmt)

    def get_by_sku(self, sku: str):
        stmt = select(Product).where(
            Product.sku == sku
        )

        return self.db.scalar(stmt)

    def list_all(self):
        stmt = select(Product).order_by(
            Product.created_at.desc()
        )

        return list(
            self.db.scalars(stmt).all()
        )

    def create(self, product: Product):
        self.db.add(product)

        return product

    def update(self, product: Product):
        return product

    def delete(self, product: Product):
        self.db.delete(product)
