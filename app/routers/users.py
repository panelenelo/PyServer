from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from fastapi.params import Body
from app.model.model import UsersCreate, Users, UsersRead
from app.database import get_session, insert_user
from sqlmodel import Session, select, desc, delete


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

@router.get("/signup")
async def getCreateUser():
    return {"data": "Creation page"}

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def postCreateUser(user: UsersCreate):
    user_obj = user.model_dump()
    return {"User": user_obj}

# Testing routes
@router.post("/testing/fill-users", status_code=status.HTTP_201_CREATED)
async def postFillUsers(session: Session=Depends(get_session)):
    # region Creating different users
    new_user = UsersCreate(email="gabelado@mango.br", name="Gabo", age=45, interest="Mangos", password="two2s")
    insert_user(new_user, session)
    new_user = UsersCreate(email="tradeu@mango.br", name="Tradeu", age=17, interest="Pines", password="Roubar")
    insert_user(new_user, session)
    new_user = UsersCreate(email="razeli@mango.br", name="Razeli", age=56, interest="kilimanjo", password="games")
    insert_user(new_user, session)
    new_user = UsersCreate(email="spaghetthi@mango.br", name="Spaghett", age=27, interest="Pesto", password="wahtc")
    insert_user(new_user, session)
    # endregion
    return {"Data": new_user}

