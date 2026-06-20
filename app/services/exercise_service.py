from fastapi import HTTPException

from app.models.exercise import Exercise
from app.repositories.exercise import exercise_repository

class ExerciseService:
    def create(self, db, exercise_in):
        exercise = Exercise(
            name=exercise_in.name,
            description=exercise_in.description,
            muscle_group=exercise_in.muscle_group
            )
        return exercise_repository.create(db, exercise)
    
    def get_all(self, db):
        exercises = exercise_repository.get_all(db)
        return exercises

    def update(self, db, exercise_id, exercise_in):
        exercise = exercise_repository.get(db, exercise_id)
        if not exercise:
            raise HTTPException(status_code=404, detail="Exercise not found")
        exercise.name = exercise_in.name
        exercise.description = exercise_in.description
        exercise.muscle_group = exercise_in.muscle_group
        return exercise_repository.update(db, exercise)

    def delete(self, db, exercise_id):
        exercise = exercise_repository.get(db, exercise_id)
        if not exercise:
            raise HTTPException(status_code=404, detail="Exercise not found")
        exercise_repository.delete(db, exercise)
        return {"detail" : "Exercise deleted successfully"}
    
exercise_service = ExerciseService()