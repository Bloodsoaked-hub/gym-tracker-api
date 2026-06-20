from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps.db import get_db
from app.api.deps.auth import get_current_user
from app.models.user import User
from app.models.workout import Workout
from app.schemas.workout import WorkoutCreate, WorkoutOut
from app.repositories.workout import workout_repository

router = APIRouter()

@router.post("/", response_model=WorkoutOut)
def create_workout(workout_in: WorkoutCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workout = Workout(
        user_id=current_user.id,
        date=workout_in.date,
        duration_minutes=workout_in.duration_minutes,
        notes=workout_in.notes
    )
    return workout_repository.create(db, workout)

@router.get("/", response_model=list[WorkoutOut])
def list_workouts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workout_repository.get_user_workouts(db, current_user.id)
    
@router.get("/{workout_id}", response_model=WorkoutOut)
def get_workout(workout_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workout = workout_repository.get_user_workout(db, workout_id, current_user.id)
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout

@router.delete("/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workout = workout_repository.get_user_workout(db, workout_id, current_user.id)
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    workout_repository.delete(db, workout)
    return {"detail": "Workout deleted successfully"}