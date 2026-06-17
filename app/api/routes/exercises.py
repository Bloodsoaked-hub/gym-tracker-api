from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.api.deps.db import get_db
from app.api.deps.auth import get_current_user
from app.models.user import User
from app.models.exercise import Exercise
from app.schemas.exercise import ExerciseCreate, ExerciseOut

router = APIRouter()

@router.post("/", response_model=ExerciseOut)
def create_exercise(exercise_in: ExerciseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    exercise = Exercise(
        name=exercise_in.name,
        description=exercise_in.description,
        muscle_group=exercise_in.muscle_group
    )

    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise

@router.get("/", response_model=list[ExerciseOut])
def list_exercises(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    exercises = db.query(Exercise).all()
    return exercises

@router.put("/{exercise_id}", response_model=ExerciseOut)
def update_exercise(exercise_id: int, exercise_in: ExerciseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    exercise.name = exercise_in.name
    exercise.description = exercise_in.description
    exercise.muscle_group = exercise_in.muscle_group
    db.commit()
    db.refresh(exercise)
    return exercise

@router.delete("/{exercise_id}")
def delete_exercise(exercise_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    db.delete(exercise)
    db.commit()
    return {"detail" : "Exercise deleted successfully"}