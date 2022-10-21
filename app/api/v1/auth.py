from fastapi import APIRouter, HTTPException, Depends
from app.core.db import init_mongo_engine
from app.schemas.users import User, TokenSchema
from fastapi.security import (
    OAuth2PasswordRequestForm,
)
from app.core.security import create_access_token, create_refresh_token
from app.settings import get_app_settings


router = APIRouter(prefix="/auth", tags=["Authentication"])
engine = init_mongo_engine()
settings = get_app_settings()


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> TokenSchema:
    user: User | None = await engine.find_one(User, User.username == form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not user.verify_password(form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return TokenSchema(
        access_token=create_access_token(str(user.id)),
        refresh_token=create_refresh_token(str(user.id)),
        token_type="Bearer",
        scope="create",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )
