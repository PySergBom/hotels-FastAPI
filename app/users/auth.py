from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr
from starlette import status

from app.config import settings
from app.users.dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not (user and verify_password(password, user.hashed_password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
