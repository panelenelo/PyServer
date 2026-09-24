from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.posts import router as post_router
from app.routers.test  import router as test_router
from app.database import create_db_and_tables, engine
from app.redis_utils import create_redis_client, create_redis_pool

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    pool = create_redis_pool()
    client = create_redis_client(pool=pool)
    app.state.redis_pool = pool
    app.state.redis = client
    if client.ping():
        print("Ping sucessful")
    yield
    engine.dispose()
    await client.aclose()
    await pool.aclose()

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(post_router)
app.include_router(test_router)

@app.get("/")
async def root():
    return {"Home": "Page"}





# if __name__ == "__main__":
#     main()


