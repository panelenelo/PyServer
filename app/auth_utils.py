from typing import Annotated
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHashError
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    pass

def passHashing(password: str) -> str:
    ph = PasswordHasher()
    hashed = ph.hash(password)
    return hashed

def verifyPass(stored_hash: str, password: str) -> bool:
    ph = PasswordHasher()
    try:
        return ph.verify(stored_hash, password)        
    except VerifyMismatchError:
        raise
    except InvalidHashError:
        raise
    except VerificationError:
        raise

