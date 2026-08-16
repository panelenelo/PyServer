from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Body
from app.model.model import UsersCreate
from sqlmodel import Field, SQLModel
from app.database import get_session


router = APIRouter()

@router.get("/users")
async def getUsers():
    
    return {"data": "Users"}

@router.get("/singup")
async def getCreateUser():
    return {"data": "Creation page"}

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def postCreateUser(user: UsersCreate):
    user_obj = user.model_dump()
    return {"User": user_obj}

