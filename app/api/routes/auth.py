from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.repositories.user import user_repository
from app.api.deps.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.schemas.auth import LoginRequest, Token
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = user_repository.get_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email, 
        hashed_password=hash_password(user.password))
    return user_repository.create(db, new_user)

@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):

    user = user_repository.get_by_email(db, data.email)
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}