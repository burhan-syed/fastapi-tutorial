import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app.config import settings
from app.database import get_db, Base


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # , connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


