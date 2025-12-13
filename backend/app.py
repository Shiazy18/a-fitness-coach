from fastapi import FastAPI
from routers.user_routes import router as user_router
from routers.plan_routes import router as plan_router

app = FastAPI(title="AI Fitness Coach API", version="1.0.0")

app.include_router(user_router)
app.include_router(plan_router)

@app.get("/")
def home():
    return {"message": "AI Fitness Coach Backend is running!"}
