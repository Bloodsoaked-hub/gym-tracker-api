from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps.db import get_db
from app.api.deps.auth import get_current_user
from app.models.user import User
from app.schemas.workout_exercises import WorkoutExerciseCreate, WorkoutExerciseOut
from app.services.workout_exercise_service import workout_exercise_service

router = APIRouter()

@router.post("/", response_model=WorkoutExerciseOut)
def add_exercise_to_workout(workout_id: int, exercise_in: WorkoutExerciseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workout_exercise_service.add_exercise_to_workout(db, exercise_in, workout_id, current_user.id)
    

@router.get("/", response_model=list[WorkoutExerciseOut])
def list_workout_exercises(workout_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workout_exercise_service.get_workout_exercises(db, workout_id, current_user.id)