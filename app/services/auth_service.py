from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.repositories.user import user_repository
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserCreate
from app.schemas.auth import LoginRequest

class AuthService:
    def register(self, db: Session, user_in: UserCreate):
        existing_user = user_repository.get_by_email(db, user_in.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        new_user = User(
            email=user_in.email,
            hashed_password=hash_password(user_in.password)
        )
        return user_repository.create(db, new_user)
    
    def login(self, db: Session, data: LoginRequest):
        user = user_repository.get_by_email(db, data.email)
        if not user or not verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token, "token_type": "bearer"}
    
auth_service = AuthService()