import os
from dotenv import load_dotenv
from sqlmodel import Session, create_engine

POSTGRES_USER = os.getenv("PGRS_USER")
POSTGRES_PASSWORD = os.getenv("PGRS_PASSWORD")
POSTGRES_DB = os.getenv("PGRS_DB")
POSTGRES_HOST = os.getenv("PGRS_HOST", "localhost")
POSTGRES_PORT = os.getenv("PGRS_PORT", "5432")

DATABASE_URL = (
    f"postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

def get_session():
    with Session(engine) as session:
        yield session