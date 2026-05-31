from uuid import UUID

from pydantic import BaseModel


class LowStockProduct(BaseModel):
    id: UUID
    name: str
    stock_quantity: int


class DashboardResponse(BaseModel):
    total_products: int
    total_customers: int
    total_orders: int

    low_stock_products: list[
        LowStockProduct
    ]