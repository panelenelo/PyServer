import os
from dotenv import load_dotenv
from sqlmodel import Session, create_engine, SQLModel
from app.model import model

# Load the .env
load_dotenv()

POSTGRES_USER = os.getenv("PGRS_USER")
POSTGRES_PASSWORD = os.getenv("PGRS_PASS")
POSTGRES_DB = os.getenv("PGRS_DB")
POSTGRES_HOST = os.getenv("PGRS_HOST", "localhost")
POSTGRES_PORT = os.getenv("PGRS_PORT", "5432")

DATABASE_URL = (
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{"0.0.0.0"}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
