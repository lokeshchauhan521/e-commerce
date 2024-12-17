from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from passlib.context import CryptContext
from ..config.environment import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class TokenData(BaseModel):
    userEmail: str | None = None


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)
        )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> TokenData:
    if not token:
        return TokenData(userEmail=None)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email: Optional[str] = payload.get("userEmail")
        if not user_email:
            return TokenData(userEmail=None)
        return TokenData(userEmail=user_email)
    except:
        return TokenData(userEmail=None)
