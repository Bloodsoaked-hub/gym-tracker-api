from sqlalchemy.orm import Session
from app.models.workout_exercises import WorkoutExercise
from app.repositories.base import BaseRepository

class WorkoutExerciseRepository(BaseRepository):
    def __init__(self):
        super().__init__(WorkoutExercise)

workout_exercise_repository = WorkoutExerciseRepository()