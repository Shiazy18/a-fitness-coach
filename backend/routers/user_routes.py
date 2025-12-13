from fastapi import APIRouter, HTTPException, status
from models.user import User
from services.db_services import create_user, get_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def add_user(user: User):
    try:
        created_user = create_user(user.dict())
        return created_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}")
def fetch_user(user_id: str):
    try:
        user = get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


