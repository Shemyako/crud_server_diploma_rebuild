from fastapi import APIRouter
from sqlalchemy import insert
# from models import *
from . import pydantic_models
import db

### 
# TO DO
# добавить проверку вводимых данных
# staff
# dog
# course
# lesson
# type_of_lesson
# adv
###


post_router = APIRouter()  


@post_router.post("/staff/")
async def create_staff(staff: pydantic_models.Staff):
    # staff.id = None
    # query = db.staff.insert().
    query = insert(db.staff)
    # print(staff.dict())

    return await db.database.execute(query, staff.dict())


@post_router.post("/dog/")
async def create_dog(dog: pydantic_models.Dogs):
    dog.id = None

    query = db.staff.select()

    return await db.database.fetch_all(query)


@post_router.post("/course/")
async def create_course(course: pydantic_models.Courses):
    course.id = None

    return course


@post_router.post("/lesson/")
async def create_lesson(lesson: pydantic_models.Lessons):
    lesson.id = None
    
    return lesson


@post_router.post("/type_of_lesson/")
async def create_type_of_lesson(type_of_lesson: pydantic_models.TypesOfLesson):
    type_of_lesson.id = None
    
    return type_of_lesson


@post_router.post("/adv/")
async def create_adv(adv: pydantic_models.Advertisements):
    adv.id = None
    
    return adv
