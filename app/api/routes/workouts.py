from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps.db import get_db
from app.api.deps.auth import get_current_user
from app.models.user import User
from app.models.workout import Workout
from app.schemas.workout import WorkoutCreate, WorkoutOut

router = APIRouter()

@router.post("/", response_model=WorkoutOut)
def create_workout(workout_in: WorkoutCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workout = Workout(
        user_id=current_user.id,
        date=workout_in.date,
        duration_minutes=workout_in.duration_minutes,
        notes=workout_in.notes
    )
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

@router.get("/", response_model=list[WorkoutOut])
def list_workouts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Workout).filter(Workout.user_id == current_user.id).all()
    
@router.get("/{workout_id}", response_model=WorkoutOut)
def get_workout(workout_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workout = db.query(Workout).filter(Workout.id == workout_id, Workout.user_id == current_user.id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout

@router.delete("/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workout = db.query(Workout).filter(Workout.id == workout_id, Workout.user_id == current_user.id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    db.delete(workout)
    db.commit()
    return {"detail": "Workout deleted successfully"}