from pydantic import BaseModel

class User(BaseModel):
    id: str
    age: int
    weight: float
    height: float
    goal: str
    activity_level: str
    diet_preference: str
