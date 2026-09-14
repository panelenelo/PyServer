from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from fastapi.params import Body
from app.model.model import UsersCreate, Users, UsersRead, UsersLogin
from app.database import get_session, insert_user, get_user_pass, get_user_with_email
from sqlmodel import Session, select, desc, delete
from app import auth_utils
from app import custom_exceptions
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHashError


router = APIRouter()


# get last 5 created users
@router.get("/users")
async def getUsers(session: Session=Depends(get_session)):
    statement = (
        select(Users)
        .order_by(desc(Users.created))
        .limit(5)
    )
    results = session.exec(statement)
    users = results.all()
    return users

@router.get("/users/{id}", response_model=UsersRead)
async def getUserById(id: int, session: Session=Depends(get_session)):
    user = session.get(Users, id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

@router.get("/signup")
async def getCreateUser():
    return {"Data": "Creation page"}

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def postCreateUser(user: UsersCreate, session: Session=Depends(get_session)):
    new_user = user.model_dump()
    hashed = auth_utils.passHashing(user.password)
    new_user["password"] = hashed
    try:
        get_user_with_email(user.email, session)
    except custom_exceptions.EmailNotInDatabase:
        insert_user(UsersCreate(**new_user), session)
        return {"User": new_user}
    else:
        raise HTTPException(
            status_code=409,
            detail="Email already in use"
        )

@router.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteUserById(id: int, session: Session=Depends(get_session)):
    user = session.get(Users, id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    session.delete(user)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)




# Testing routes
@router.post("/testing/fill-users", status_code=status.HTTP_201_CREATED)
async def postFillUsers(session: Session=Depends(get_session)):
    # region Creating different users
    new_user = UsersCreate(email="gabelado@mango.br", name="Gabo", age=45, interest="Mangos", password="two2s")
    hashed = auth_utils.passHashing(new_user.password)
    new_user.password = hashed
    insert_user(new_user, session)
    new_user = UsersCreate(email="tradeu@mango.br", name="Tradeu", age=17, interest="Pines", password="Roubar")
    hashed = auth_utils.passHashing(new_user.password)
    new_user.password = hashed
    insert_user(new_user, session)
    new_user = UsersCreate(email="razeli@mango.br", name="Razeli", age=56, interest="kilimanjo", password="games")
    hashed = auth_utils.passHashing(new_user.password)
    new_user.password = hashed
    insert_user(new_user, session)
    new_user = UsersCreate(email="spaghetthi@mango.br", name="Spaghett", age=27, interest="Pesto", password="wahtc")
    hashed = auth_utils.passHashing(new_user.password)
    new_user.password = hashed
    insert_user(new_user, session)
    # endregion
    return {"Data": new_user}

@router.delete("/testing/reset-users", status_code=status.HTTP_204_NO_CONTENT)
async def deleteUsersAll(session: Session=Depends(get_session)):
    session.exec(delete(Users))
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/testing/pass-verify")
async def getTestVerifyPass(payload: UsersLogin, session: Session=Depends(get_session)):
    user = payload.model_dump()
    try:
        stored_password = get_user_pass(payload.email, session)
        verification = auth_utils.verifyPass(stored_password, payload.password)
        #.check_needs_rehash()
    except custom_exceptions.EmailNotInDatabase:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )    
    except VerifyMismatchError:
        raise HTTPException(
            status_code=404,
            detail="Email or password wrong"
        )
    except InvalidHashError:
        raise HTTPException(
            status_code=404,
            detail="Invalid Hash Error"
        )
    except VerificationError:
        raise HTTPException(
            status_code=404,
            detail="Verification Error"
        )
    else:
        return {"Verification": "OK"}
