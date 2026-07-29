from fastapi import FastAPI, Response, status, HTTPException


@app.get("/posts")
async def getPosts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def postCreatePosts(payload: Post):
    post_dict = payload.model_dump()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": my_posts}

@app.get("/posts/{id}")
async def getPostById(id: int):
    return {"post detail": f"Post {id}"}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletePostById(id: int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", status_code=status.HTTP_206_PARTIAL_CONTENT)
def putPostById(id: int, post: Post):
    return Response(status_code=status.HTTP_206_PARTIAL_CONTENT)
