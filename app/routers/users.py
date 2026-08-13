from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Body
from app.model.model import User
from random import randrange

router = APIRouter()

@router.get("/users")
async def getUsers():
    return {"data": "Users"}

@router.get("/singup")
async def getCreateUser():
    return {"data": "Creation page"}

@router.post("/signup")
async def postCreateUser(user: User):
    user_obj = user.model_dump()
    return {"User": user_obj}
