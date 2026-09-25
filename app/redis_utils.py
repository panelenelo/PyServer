import os
import redis.asyncio as aredis
from fastapi import Request
from dotenv import load_dotenv

# Load the .env
load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASS = os.getenv("REDIS_PASS")

def create_redis_pool() -> aredis.BlockingConnectionPool:
    return aredis.BlockingConnectionPool(
        host="localhost",
        port=REDIS_PORT,
        max_connections=8,  
        timeout=5,           
        decode_responses=True,
    )

def create_redis_client(pool: aredis.BlockingConnectionPool) -> aredis.Redis:
    return aredis.Redis(connection_pool=pool)


# Return the redis client
async def get_redis(request: Request) -> aredis.Redis:
    return request.app.state.redis