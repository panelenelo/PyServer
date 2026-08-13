from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Post(BaseModel):
    # id:         int
    title:      str
    content:    str
    published:  bool = True
    rating:     Optional[int] = None

class User(BaseModel):
    # id:         int
    name:       str
    age:        int
    interest:   str
    created:    datetime = Field(default_factory=datetime.now)

