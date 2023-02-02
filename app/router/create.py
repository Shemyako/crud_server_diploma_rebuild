from fastapi import APIRouter
# from models import *
import db

create_router = APIRouter()  


@create_router.post("/staff/")
async def create_staff():
    pass


@create_router.post("/dog/")
async def create_dog():
    pass


@create_router.post("/course/")
async def create_course():
    pass


@create_router.post("/lesson/")
async def create_lesson():
    pass


@create_router.post("/type_of_lesson/")
async def create_type_of_lesson():
    pass


@create_router.post("/adv/")
async def create_adv():
    pass
