from fastapi import APIRouter
from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.exercises import router as exercises_router
from app.api.routes.workouts import router as workouts_router
from app.api.routes.workout_exercises import router as workout_exercises_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(exercises_router, prefix="/exercises", tags=["exercises"])
api_router.include_router(workouts_router, prefix="/workouts", tags=["workouts"])
api_router.include_router(workout_exercises_router, prefix="/workouts/{workout_id}/exercises", tags=["workout_exercises"])