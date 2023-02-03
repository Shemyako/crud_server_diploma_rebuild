from fastapi import APIRouter
# from models import *
from . import pydantic_models
import db

create_router = APIRouter()  


@create_router.post("/staff/")
async def create_staff(staff: pydantic_models.Staff):
    query = db.typesOfLesson.select()
    return await db.database.fetch_all(query)


@create_router.post("/dog/")
async def create_dog(dog: pydantic_models.Dogs):
    return dog


@create_router.post("/course/")
async def create_course(course: pydantic_models.Courses):
    return course


@create_router.post("/lesson/")
async def create_lesson(lesson: pydantic_models.Lessons):
    return lesson


@create_router.post("/type_of_lesson/")
async def create_type_of_lesson(type_of_lesson: pydantic_models.TypesOfLesson):
    return type_of_lesson


@create_router.post("/adv/")
async def create_adv(adv: pydantic_models.Advertisements):
    return adv
