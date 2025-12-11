from fastapi import APIRouter
from services.openai_service import generate_fitness_plan
from services.db_service import get_user

router = APIRouter(prefix="/plan")

@router.get("/{user_id}")
def generate_plan(user_id: str):
    user = get_user(user_id)
    plan = generate_fitness_plan(user)
    return {"plan": plan}
