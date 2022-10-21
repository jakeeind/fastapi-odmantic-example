from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.core.db import init_mongo_engine
from app.core.depends import get_current_user
from app.schemas.users import User, UserCreate

router = APIRouter(prefix="/users", tags=["User"])
engine = init_mongo_engine()


@router.post("/register", response_model=User, name="create user")
async def register(user: UserCreate):
    exsiting_user: User | None = await engine.find_one(
        User, User.username == user.username
    )
    if exsiting_user is not None:
        raise HTTPException(403, detail="user already exists")
    new_user = User(**user.dict())
    new_user.set_password(user.password)
    await engine.save(new_user)
    return new_user


@router.get(
    "/users",
    response_model=List[User],
    name="get users",
    # dependencies=[Depends(get_current_user)],
)
async def get_users():
    users: List[User] = await engine.find(User)
    return users
