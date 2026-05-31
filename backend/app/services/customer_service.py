from sqlalchemy.orm import Session

from app.core.exceptions import (
    CustomerNotFoundError,
    DuplicateEmailError,
)

from app.models.customer import Customer

from app.repositories.customer_repository import (
    CustomerRepository,
)

from app.schemas.customer import (
    CustomerCreate,
)


class CustomerService:
    def __init__(self, db: Session):
        self.repo = CustomerRepository(db)

    def add_customer(
        self,
        payload: CustomerCreate,
    ):
        existing_customer = (
            self.repo.get_by_email(
                payload.email
            )
        )

        if existing_customer:
            raise DuplicateEmailError()

        customer = Customer(
            full_name=payload.full_name,
            email=payload.email,
            phone=payload.phone,
        )

        self.repo.create(customer)

        self.repo.db.commit()
        self.repo.db.refresh(customer)

        return customer

    def list_customers(self):
        return self.repo.list_all()

    def get_customer(
        self,
        customer_id,
    ):
        customer = self.repo.get_by_id(
            customer_id
        )

        if not customer:
            raise CustomerNotFoundError()

        return customer

    def remove_customer(
        self,
        customer_id,
    ):
        customer = self.get_customer(
            customer_id
        )

        self.repo.delete(customer)

        self.repo.db.commit() 