from sqlalchemy.orm import Session
from app.models.exercise import Exercise
from app.repositories.base import BaseRepository

class ExerciseRepository(BaseRepository):
    def __init__(self):
        super().__init__(Exercise)

exercise_repository = ExerciseRepository()