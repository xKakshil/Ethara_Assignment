from decimal import Decimal

from sqlalchemy.orm import Session

from app.core.exceptions import (
    CustomerNotFoundError,
    ProductNotFoundError,
    OrderNotFoundError,
    InsufficientStockError,
)

from app.models.order import Order
from app.models.order_item import OrderItem

from app.repositories.customer_repository import (
    CustomerRepository,
)

from app.repositories.product_repository import (
    ProductRepository,
)

from app.repositories.order_repository import (
    OrderRepository,
)

from app.repositories.order_item_repository import (
    OrderItemRepository,
)

from app.schemas.order import (
    OrderCreate,
)


class OrderService:
    def __init__(self, db: Session):
        self.db = db

        self.customer_repo = CustomerRepository(db)
        self.product_repo = ProductRepository(db)

        self.order_repo = OrderRepository(db)
        self.order_item_repo = OrderItemRepository(db)

    def create_order(
        self,
        payload: OrderCreate,
    ):
        customer = self.customer_repo.get_by_id(
            payload.customer_id
        )

        if not customer:
            raise CustomerNotFoundError()

        total_amount = Decimal("0.00")

        order_items_data = []

        for item in payload.items:

            product = self.product_repo.get_by_id(
                item.product_id
            )

            if not product:
                raise ProductNotFoundError()

            if product.stock_quantity < item.quantity:
                raise InsufficientStockError()

            subtotal = (
                product.price * item.quantity
            )

            total_amount += subtotal

            order_items_data.append(
                {
                    "product": product,
                    "quantity": item.quantity,
                    "unit_price": product.price,
                    "subtotal": subtotal,
                }
            )

        try:

            order = Order(
                customer_id=payload.customer_id,
                total_amount=total_amount,
            )

            self.order_repo.create(order)

            self.db.flush()

            for item_data in order_items_data:

                order_item = OrderItem(
                    order_id=order.id,
                    product_id=item_data[
                        "product"
                    ].id,
                    quantity=item_data[
                        "quantity"
                    ],
                    unit_price=item_data[
                        "unit_price"
                    ],
                    subtotal=item_data[
                        "subtotal"
                    ],
                )

                self.order_item_repo.create(
                    order_item
                )

                item_data[
                    "product"
                ].stock_quantity -= item_data[
                    "quantity"
                ]

            self.db.commit()

            self.db.refresh(order)

            return order

        except Exception:
            self.db.rollback()
            raise

    def get_order(
        self,
        order_id,
    ):
        order = self.order_repo.get_by_id(
            order_id
        )

        if not order:
            raise OrderNotFoundError()

        return order

    def list_orders(self):
        return self.order_repo.list_all()

    def remove_order(
        self,
        order_id,
    ):
        order = self.get_order(order_id)

        try:
            self.order_repo.delete(order)

            self.db.commit()

        except Exception:
            self.db.rollback()
            raise