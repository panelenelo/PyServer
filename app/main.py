from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.posts import router as post_router
from app.routers.test  import router as test_router
from app.database import create_db_and_tables

create_db_and_tables()

app = FastAPI()

app.include_router(user_router)
app.include_router(post_router)
app.include_router(test_router)

@app.get("/")
async def root():
    return {"Home": "Page"}



# if __name__ == "__main__":
#     main()


