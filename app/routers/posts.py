from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from fastapi.params import Body
from app.model.model import PostsCreate, Posts, PostsRead
from random import randrange
from app.database import get_session, insert_post
from sqlmodel import Session, select, desc, delete

router = APIRouter()

#get last 5 created posts
@router.get("/posts")
async def getPosts(session: Session=Depends(get_session)):
    statement = (
        select(Posts)
        .order_by(desc(Posts.created))
        .limit(5)
    )
    results = session.exec(statement)
    posts = results.all()

    return posts

@router.get("/posts/{id}", response_model=PostsRead)
async def getPostById(id: int, session: Session=Depends(get_session)):
    post = session.get(Posts, id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    return post

@router.post("/posts", status_code=status.HTTP_201_CREATED)
async def postCreatePosts(payload: PostsCreate, session: Session=Depends(get_session)):
    new_post = insert_post(payload, session)
    return {"Data": new_post}

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletePostById(id: int, session: Session=Depends(get_session)):
    post = session.get(Posts, id)
    if not post:
            raise HTTPException(
                status_code=404,
                detail="Post not found"
            )
    session.delete(post)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{id}", status_code=status.HTTP_206_PARTIAL_CONTENT)
async def putPostById(id: int, post: PostsCreate):
    return Response(status_code=status.HTTP_206_PARTIAL_CONTENT)


# Testing routes
@router.delete("/testing/reset-posts", status_code=status.HTTP_204_NO_CONTENT)
async def deletePostAll(session: Session=Depends(get_session)):
    session.exec(delete(Posts))
    session.commit()    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post("/testing/fill-posts", status_code=status.HTTP_201_CREATED)
async def postCreatePosts(session: Session=Depends(get_session)):
    # The while here is just so i can minimize it in VSCode
    while True:
        new_post = Posts(title="New one", content="Another day in the valley")
        insert_post(new_post, session)
        new_post = Posts(title="The comeback!", content="And thanne he trauayled agayne to mete his fader and moder after the grete warre")
        insert_post(new_post, session)
        new_post = Posts(title="Not a happy end", content="The war still waging, and his light wanning")
        insert_post(new_post, session)
        new_post = Posts(title="Clear sky", content="Clear sky day, the fields full of green hay, but justice still came")
        insert_post(new_post, session)
        new_post = Posts(title="A name", content="The story of a person with a name, whose name is remembered with happines, happiness that it will never be heard again")
        insert_post(new_post, session)
        break

    return {"Data": new_post}