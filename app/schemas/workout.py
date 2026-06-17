from pydantic import BaseModel, ConfigDict
from datetime import datetime

class WorkoutCreate(BaseModel):
    date: datetime
    duration_minutes: int | None = None
    notes: str | None = None

class WorkoutOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date: datetime
    duration_minutes: int | None = None
    notes: str | None = None
