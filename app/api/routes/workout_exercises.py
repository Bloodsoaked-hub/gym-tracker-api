from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps.db import get_db
from app.api.deps.auth import get_current_user
from app.models.user import User
from app.models.workout import Workout
from app.models.exercise import Exercise
from app.models.workout_exercises import WorkoutExercise
from app.schemas.workout_exercises import WorkoutExerciseCreate, WorkoutExerciseOut

router = APIRouter()

@router.post("/", response_model=WorkoutExerciseOut)
def add_exercise_to_workout(workout_id: int, exercise_in: WorkoutExerciseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workout = db.query(Workout).filter(Workout.id == workout_id, Workout.user_id == current_user.id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    exercise = db.query(Exercise).filter(Exercise.id == exercise_in.exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    workout_exercise = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_in.exercise_id,
        sets=exercise_in.sets,
        reps=exercise_in.reps,
        weight=exercise_in.weight
    )

    db.add(workout_exercise)
    db.commit()
    db.refresh(workout_exercise)
    return {
        "id": workout_exercise.id,
        "exercise_id": exercise.id,
        "exercise_name": exercise.name,
        "sets": workout_exercise.sets,
        "reps": workout_exercise.reps,
        "weight": workout_exercise.weight
    }
    

@router.get("/", response_model=list[WorkoutExerciseOut])
def list_workout_exercises(workout_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    workout = db.query(Workout).filter(Workout.id == workout_id, Workout.user_id == current_user.id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    return [
    {
        "id": we.id,
        "exercise_id": we.exercise_id,
        "exercise_name": we.exercise.name,
        "sets": we.sets,
        "reps": we.reps,
        "weight": we.weight
    }
    for we in workout.exercises
]