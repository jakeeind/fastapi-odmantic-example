from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from odmantic import ObjectId
from app.schemas.users import User
from app.core.db import init_mongo_engine
from ..settings import get_app_settings

reuseable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
settings = get_app_settings()
engine = init_mongo_engine()


async def get_current_user(token: str = Depends(reuseable_oauth2)) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    print(payload.get("sub"))
    user: User | None = await engine.find_one(User, User.id == ObjectId(payload.get("sub")))
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
