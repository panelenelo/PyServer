from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Body
from app.model.model import Post
from random import randrange

router = APIRouter()