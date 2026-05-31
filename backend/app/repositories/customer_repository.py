from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, customer_id: UUID):
        stmt = select(Customer).where(
            Customer.id == customer_id
        )

        return self.db.scalar(stmt)

    def get_by_email(self, email: str):
        stmt = select(Customer).where(
            Customer.email == email
        )

        return self.db.scalar(stmt)

    def list_all(self):
        stmt = select(Customer).order_by(
            Customer.created_at.desc()
        )

        return list(
            self.db.scalars(stmt).all()
        )

    def create(self, customer: Customer):
        self.db.add(customer)

        return customer

    def delete(self, customer: Customer):
        self.db.delete(customer)