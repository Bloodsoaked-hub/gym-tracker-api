from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps.db import get_db
from app.schemas.user import UserCreate, UserOut
from app.schemas.auth import LoginRequest, Token
from app.services.auth_service import auth_service

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.register(db, user)

@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return auth_service.login(db, data)