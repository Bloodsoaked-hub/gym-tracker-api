from pydantic import BaseModel, ConfigDict

class WorkoutExerciseCreate(BaseModel):
    exercise_id: int
    sets: int | None = None
    reps: int | None = None
    weight: float | None = None

class WorkoutExerciseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    exercise_id: int
    exercise_name: str
    sets: int | None = None
    reps: int | None = None
    weight: float | None = None