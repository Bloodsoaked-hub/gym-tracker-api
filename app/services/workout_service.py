from fastapi import HTTPException

from app.models.workout import Workout
from app.repositories.workout import workout_repository

class WorkoutService:
    def create(self, db, workout_in, user_id):
        workout = Workout(
            user_id=user_id,
            date=workout_in.date,
            duration_minutes=workout_in.duration_minutes,
            notes=workout_in.notes
        )
        return workout_repository.create(db, workout)
    
    def get_all(self, db, user_id):
        return workout_repository.get_user_workouts(db, user_id)

    def get(self, db, workout_id, user_id):
        workout = workout_repository.get_user_workout(db, workout_id, user_id)
        if not workout:
            raise HTTPException(status_code=404, detail="Workout not found")
        return workout

    def delete(self, db, workout_id, user_id):
        workout = workout_repository.get_user_workout(db, workout_id, user_id)
        if not workout:
            raise HTTPException(status_code=404, detail="Workout not found")
        workout_repository.delete(db, workout)
        return {"detail": "Workout deleted successfully"}

workout_service = WorkoutService()