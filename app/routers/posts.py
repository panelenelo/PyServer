from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from fastapi.params import Body
from app.model.model import PostsCreate, Posts
from random import randrange
from app.database import get_session, insert_post
from sqlmodel import Session

router = APIRouter()

@router.get("/posts")
async def getPosts():
    return {"Data": "The posts"}

@router.get("/posts/{id}")
async def getPostById(id: int, session: Session=Depends(get_session)):
    post = session.get(Posts, id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    return {"Data": post}

@router.post("/posts", status_code=status.HTTP_201_CREATED)
async def postCreatePosts(payload: PostsCreate, session: Session=Depends(get_session)):
    new_post = insert_post(payload, session)
    return {"Data": new_post}

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletePostById(id: int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{id}", status_code=status.HTTP_206_PARTIAL_CONTENT)
async def putPostById(id: int, post: PostsCreate):
    return Response(status_code=status.HTTP_206_PARTIAL_CONTENT)
