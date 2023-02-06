from fastapi import APIRouter
from sqlalchemy import insert
# from models import *
from . import pydantic_models
import db


get_router = APIRouter()  


@get_router.get("/staff/")
async def get_staff(id:int = None):
    # print(id)
    query = db.staff.select().where(db.staff.c.id == id) if id \
        else db.staff.select()
    return await db.database.fetch_all(query)


@get_router.get("/dog/")
async def get_dog(id:int = None):
    query = db.dogs.select().where(db.dogs.c.id == id) if id \
        else db.dogs.select()
    return await db.database.fetch_all(query)


@get_router.get("/course/")
async def get_course(id:int = None):
    query = db.courses.select().where(db.courses.c.id == id) if id \
        else db.courses.select()
    return await db.database.fetch_all(query)


@get_router.get("/lesson/")
async def get_lesson(id:int = None):
    query = db.lessons.select().where(db.lessons.c.id == id) if id \
        else db.lessons.select()
    return await db.database.fetch_all(query)


@get_router.get("/type_of_lesson/")
async def get_type_of_lesson(id:int = None):
    query = db.typesOfLesson.select().where(db.typesOfLesson.c.id == id) if id \
        else db.typesOfLesson.select()
    return await db.database.fetch_all(query)


@get_router.get("/adv/")
async def get_adv(id:int = None):
    query = db.advertisements.select().where(db.advertisements.c.id == id) if id \
        else db.advertisements.select()
    return await db.database.fetch_all(query)


@get_router.get("/place/")
async def get_place(id:int = None):
    query = db.places.select().where(db.places.c.id == id) if id \
        else db.places.select()
    return await db.database.fetch_all(query)


### !
@get_router.get("/user/{user_id}/dogs")
async def get_dogs_of_user(user_id:int = None):
    query = db.places.select().where(db.places.c.id == id) if id \
        else db.places.select()
    return await db.database.fetch_all(query)


### !
@get_router.get("/dog/{dog_id}/users")
async def get_dog_owners(dog_id:int = None):
    query = db.places.select().where(db.places.c.id == id) if id \
        else db.places.select()
    return await db.database.fetch_all(query)


### !
@get_router.get("/dog/{dog_id}/courses")
async def get_dog_courses(dog_id:int = None):
    query = db.places.select().where(db.places.c.id == id) if id \
        else db.places.select()
    return await db.database.fetch_all(query)