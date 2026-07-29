from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from app.model.model import Post
from random import randrange

app = FastAPI()


@app.get("/")
async def root():
    return {"Home": "Page"}



# if __name__ == "__main__":
#     main()


