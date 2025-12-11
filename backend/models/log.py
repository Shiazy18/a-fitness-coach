from pydantic import BaseModel

class DailyLog(BaseModel):
    id: str
    user_id: str
    calories_consumed: int
    calories_burned: int
    steps: int
    notes: str | None = None
