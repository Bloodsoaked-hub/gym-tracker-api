from sqlalchemy.orm import Session
from app.models.workout import Workout
from app.repositories.base import BaseRepository

class WorkoutRepository(BaseRepository):
    def __init__(self):
        super().__init__(Workout)

    def get_user_workouts(self, db: Session, user_id: int):
        return db.query(Workout).filter(Workout.user_id == user_id).all()
    
    def get_user_workout(self, db: Session, workout_id: int, user_id: int):
        return db.query(Workout).filter(Workout.id == workout_id, Workout.user_id == user_id).first()
    
workout_repository = WorkoutRepository()