from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.api.deps.db import get_db
from app.api.deps.auth import get_current_user
from app.models.user import User
from app.schemas.exercise import ExerciseCreate, ExerciseOut
from app.services.exercise_service import exercise_service

router = APIRouter()

@router.post("/", response_model=ExerciseOut)
def create_exercise(exercise_in: ExerciseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return exercise_service.create(db, exercise_in)

@router.get("/", response_model=list[ExerciseOut])
def list_exercises(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return exercise_service.get_all(db)

@router.put("/{exercise_id}", response_model=ExerciseOut)
def update_exercise(exercise_id: int, exercise_in: ExerciseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return exercise_service.update(db, exercise_id, exercise_in)

@router.delete("/{exercise_id}")
def delete_exercise(exercise_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return exercise_service.delete(db, exercise_id)