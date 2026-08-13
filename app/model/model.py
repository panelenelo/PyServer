from typing import Optional
from sqlmodel import Field, SQLModel
# from pydantic import BaseModel, Field
from datetime import datetime

class Post(SQLModel):
    id:         int
    title:      str
    content:    str
    published:  bool = True
    rating:     Optional[int] = None

class User(SQLModel):
    id:         int
    name:       str
    age:        int
    interest:   str
    created:    datetime = Field(default_factory=datetime.now)

