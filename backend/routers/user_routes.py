from fastapi import APIRouter
from models.user import User
from services.db_services import create_user, get_user

router = APIRouter(prefix="/user")

@router.post("/")
def add_user(user: User):
    return create_user(user.dict())

@router.get("/{user_id}")
def fetch_user(user_id: str):
    return get_user(user_id)
