from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps.db import get_db
from app.api.deps.auth import get_current_user
from app.models.user import User
from app.schemas.workout import WorkoutCreate, WorkoutOut
from app.services.workout_service import workout_service

router = APIRouter()

@router.post("/", response_model=WorkoutOut)
def create_workout(workout_in: WorkoutCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workout_service.create(db, workout_in, current_user.id)

@router.get("/", response_model=list[WorkoutOut])
def list_workouts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workout_service.get_all(db, current_user.id)    

@router.get("/{workout_id}", response_model=WorkoutOut)
def get_workout(workout_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workout_service.get(db, workout_id, current_user.id)

@router.delete("/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workout_service.delete(db, workout_id, current_user.id)