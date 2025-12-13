from fastapi import APIRouter, HTTPException, status
from services.openai_services import generate_fitness_plan
from services.db_services import get_user

router = APIRouter(prefix="/plan")

@router.get("/{user_id}")
def generate_plan(user_id: str):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")
    plan = generate_fitness_plan(user)
    return {"plan": plan}
