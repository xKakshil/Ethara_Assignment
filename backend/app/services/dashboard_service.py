from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import (
    DashboardRepository,
)


class DashboardService:
    def __init__(self, db: Session):
        self.repo = DashboardRepository(db)

    def get_dashboard_data(self):
        return {
            "total_products":
                self.repo.total_products(),

            "total_customers":
                self.repo.total_customers(),

            "total_orders":
                self.repo.total_orders(),

            "low_stock_products":
                self.repo.low_stock_products(),
        }