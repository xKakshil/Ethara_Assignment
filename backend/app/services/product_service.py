from sqlalchemy.orm import Session

from app.core.exceptions import (
    DuplicateSkuError,
    ProductNotFoundError,
)

from app.models.product import Product

from app.repositories.product_repository import (
    ProductRepository,
)

from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
)


class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)

    def add_product(
        self,
        payload: ProductCreate,
    ):
        existing_product = self.repo.get_by_sku(
            payload.sku
        )

        if existing_product:
            raise DuplicateSkuError()

        new_product = Product(
            name=payload.name,
            sku=payload.sku,
            description=payload.description,
            price=payload.price,
            stock_quantity=payload.stock_quantity,
        )

        self.repo.create(new_product)

        self.repo.db.commit()
        self.repo.db.refresh(new_product)

        return new_product

    def get_product(self, product_id):
        product = self.repo.get_by_id(
            product_id
        )

        if not product:
            raise ProductNotFoundError()

        return product

    def list_products(self):
        return self.repo.list_all()

    def update_product(
        self,
        product_id,
        payload: ProductUpdate,
    ):
        product = self.get_product(product_id)

        update_data = payload.model_dump(
            exclude_unset=True
        )

        if (
            "sku" in update_data
            and update_data["sku"] != product.sku
        ):
            existing_product = self.repo.get_by_sku(
                update_data["sku"]
            )

            if existing_product:
                raise DuplicateSkuError()

        for field, value in update_data.items():
            setattr(product, field, value)

        self.repo.update(product)

        self.repo.db.commit()
        self.repo.db.refresh(product)

        return product

    def remove_product(
        self,
        product_id,
    ):
        product = self.get_product(product_id)

        self.repo.delete(product)

        self.repo.db.commit()
    