from fastapi import HTTPException

from app.models.workout_exercises import WorkoutExercise
from app.repositories.workout import workout_repository
from app.repositories.exercise import exercise_repository
from app.repositories.workout_exercise import workout_exercise_repository

class WorkoutExerciseService:
    def add_exercise_to_workout(self, db, exercise_in, workout_id, user_id):
        workout = workout_repository.get_user_workout(db, workout_id, user_id)
        if not workout:
            raise HTTPException(status_code=404, detail="Workout not found")
        exercise = exercise_repository.get(db, exercise_in.exercise_id)
        if not exercise:
            raise HTTPException(status_code=404, detail="Exercise not found")
        
        workout_exercise = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=exercise_in.exercise_id,
            sets=exercise_in.sets,
            reps=exercise_in.reps,
            weight=exercise_in.weight
        )

        workout_exercise_repository.create(db, workout_exercise)
        return {
            "id": workout_exercise.id,
            "exercise_id": exercise.id,
            "exercise_name": exercise.name,
            "sets": workout_exercise.sets,
            "reps": workout_exercise.reps,
            "weight": workout_exercise.weight
        }

    def get_workout_exercises(self, db, workout_id, user_id):
        workout = workout_repository.get_user_workout(db, workout_id, user_id)
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

workout_exercise_service = WorkoutExerciseService()