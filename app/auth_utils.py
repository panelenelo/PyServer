import uuid
from typing import Annotated
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHashError
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from os import getenv
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt
from app.model.model import Token


ph = PasswordHasher()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
load_dotenv()
jwt_key = getenv("JWT_SECRET_KEY")
jwt_algo = getenv("JWT_ALGORITHM")
refresh_exp = getenv("REFRESH_TOKEN_EXPIRE_DAYS")
access_exp = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
if (jwt_key is None) or (jwt_algo is None):
    raise RuntimeError("KEY environment variable is not set")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    pass

def passHashing(password: str) -> str:
    hashed = ph.hash(password)
    return hashed

def verifyPass(stored_hash: str, password: str) -> bool:
    try:
        return ph.verify(stored_hash, password)        
    except VerifyMismatchError:
        raise
    except InvalidHashError:
        raise
    except VerificationError:
        raise

def create_token(data: dict, duration: timedelta) -> str:
    to_encode = {**data}
    now = datetime.now(timezone.utc)
    jti = str(uuid.uuid4())
    to_encode.update({"iat":now, "exp":now+duration, "jti":jti})
    return jwt.encode(to_encode, jwt_key, algorithm=jwt_algo)

def create_refresh_token(data: dict) -> str:
    refresh_token = create_token({**data, "type":"refresh"}, timedelta(days=refresh_exp))
    # The refresh token should be stored in redis.
    return refresh_token

def create_access_token(data: dict) -> str:
    return create_token({**data, "type":"access"}, timedelta(minutes=access_exp))
    
