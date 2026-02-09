from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from src.db import(UserDB, get_async_session, RefreshTokenDB)



pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(plain_password):
    return pwd_context.hash(plain_password)