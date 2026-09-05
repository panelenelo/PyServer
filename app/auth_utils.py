from argon2 import PasswordHasher

def passHashing(password: str) -> str:
    ph = PasswordHasher()
    hashed = ph.hash(password)

    return hashed

def verifyPass(password: str) -> str:
    pass