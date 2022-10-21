from typing import List
from odmantic import Field, Model
from pydantic import BaseModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCreate(BaseModel):
    username: str
    password: str

    name: str


class User(Model):
    username: str
    password: str

    name: str
    roles: List[str] = Field(default=["user"])

    def set_password(self, plain_password):
        self.password = pwd_context.hash(plain_password)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, str(self.password))


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    scope: str
