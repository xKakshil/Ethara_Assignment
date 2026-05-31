from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.dashboard import (
    DashboardResponse,
)

from app.services.dashboard_service import (
    DashboardService,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "",
    response_model=DashboardResponse,
)
def dashboard(
    db: Session = Depends(get_db),
):
    service = DashboardService(db)

    return service.get_dashboard_data()