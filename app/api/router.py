from fastapi import APIRouter

from app.api.routes import auth, users, exercises, workouts, workout_exercises

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(exercises.router, prefix="/exercises", tags=["exercises"])
api_router.include_router(workouts.router, prefix="/workouts", tags=["workouts"])
api_router.include_router(workout_exercises.router, prefix="/workouts/{workout_id}/exercises", tags=["workout_exercises"])