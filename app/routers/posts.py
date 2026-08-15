from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Body
from app.model.model import PostsCreate
from random import randrange

router = APIRouter()

@router.get("/posts")
async def getPosts():
    return {"data": "The posts"}

@router.post("/posts", status_code=status.HTTP_201_CREATED)
async def postCreatePosts(payload: PostsCreate):
    post_dict = payload.model_dump()
    return {"data": post_dict}

@router.get("/posts/{id}")
async def getPostById(id: int):
    return {"post detail": f"Post {id}"}

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletePostById(id: int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{id}", status_code=status.HTTP_206_PARTIAL_CONTENT)
async def putPostById(id: int, post: PostsCreate):
    return Response(status_code=status.HTTP_206_PARTIAL_CONTENT)
