from sqlalchemy import select, Column, ForeignKey, Integer, Boolean, String, Text, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__ = "users"

    u_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(200), nullable=False, unique=True)
    contact = Column(String(10), nullable=False, unique=True)
    adddress = Column(Text)
    email = Column(String(225), unique=True, nullable=False)
    password = Column(String(225), nullable=False)
    is_super_user = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


