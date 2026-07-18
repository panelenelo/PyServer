from fastapi import FastAPI
from fastapi.params import Body
from model.model import Post
from random import randrange

app = FastAPI()

my_posts = [{"id":1, "title": "First Post", "content":"First Content"}]

@app.get("/")
async def root():
    return {"message": "Carm"}

@app.get("/posts")
async def getPosts():
    return {"data": my_posts}

@app.post("/posts")
async def postCreatePosts(payload: Post):
    post_dict = payload.model_dump()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": my_posts}





# if __name__ == "__main__":
#     main()


