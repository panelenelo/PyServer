from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
from pydantic import EmailStr
from datetime import datetime


#
#  Post related
#
class PostsBase(SQLModel):
    title:      str
    content:    str
    published:  bool = True
    rating:     int | None = None

class Posts(PostsBase, table=True):
    id:         int | None = Field(default=None, index=True, primary_key=True)
    created:    datetime = Field(default_factory=datetime.now)

class PostsCreate(PostsBase):
    pass

class PostsRead(PostsBase):
    created: datetime


# 
# User related
#
class UsersBase(SQLModel):
    email:      EmailStr = Field(index=True, primary_key=True)
    name:       str
    age:        int
    interest:   str | None = None

class Users(UsersBase, table=True):
    created:    datetime = Field(default_factory=datetime.now)
    password:   str

class UsersCreate(UsersBase):
    password:   str

class UsersRead(UsersBase):
    created: datetime

