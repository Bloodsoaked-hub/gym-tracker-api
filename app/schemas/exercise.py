from pydantic import BaseModel, ConfigDict

class ExerciseCreate(BaseModel):
    name: str
    description: str | None = None
    muscle_group: str | None = None

class ExerciseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None = None
    muscle_group: str | None = None
    
