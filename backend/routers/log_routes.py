#just a placeholder; will be taken care with next release
from fastapi import APIRouter
from models.log import DailyLog
from services.db_services import add_log, get_logs

router = APIRouter(prefix="/logs")

@router.post("/")
def add_daily_log(log: DailyLog):
    return add_log(log.dict())

@router.get("/{user_id}")
def fetch_logs(user_id: str):
    return get_logs(user_id)
