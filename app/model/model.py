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
    rating:     Optional[int] = None

class Posts(PostsBase, table=True):
    id:         int = Field(index=True, primary_key=True)
    created:    datetime = Field(default_factory=datetime.now)

class PostsCreate(PostsBase):
    pass

class PostsRead(PostsBase):
    created: datetime


# 
# User related
#
class UsersBase(SQLModel):
    name:       str
    age:        int
    email:      EmailStr = Field(index=True, primary_key=True)
    interest:   str

class Users(UsersBase, table=True):
    created:    datetime = Field(default_factory=datetime.now)

class UsersCreate(UsersBase):
    pass

class UsersRead(UsersBase):
    created: datetime