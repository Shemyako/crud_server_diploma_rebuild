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


@post_router.post("/type_of_lesson/")
async def create_type_of_lesson(type_of_lesson: pydantic_models.TypesOfLesson):
    # type_of_lesson.dict() - values to insert
    type_of_lesson = type_of_lesson.dict()
    # del id, so SQLAlchemy won't scold
    del type_of_lesson['id']

    # insert into talbe
    query = insert(db.typesOfLesson)
    result = await db.database.execute(query, type_of_lesson)
    return result


@post_router.post("/dog/")
async def create_dog(dog: pydantic_models.Dogs):
    dog = dog.dict()
    del dog['id']

    query = insert(db.dogs)
    result = await db.database.execute(query, dog)
    return result


@post_router.post("/userdog/")
async def create_userdog(userdog: pydantic_models.UserDog):
    userdog = userdog.dict()
    del userdog['id']

    query = insert(db.userDog)
    result = await db.database.execute(query, userdog)
    return result


@post_router.post("/lesson/")
async def create_lesson(lesson: pydantic_models.Lessons):
    lesson = lesson.dict()
    del lesson['id']

    query = insert(db.lessons)
    result = await db.database.execute(query, lesson)
    return result


@post_router.post("/staff/")
async def create_staff(staff: pydantic_models.Staff):
    staff = staff.dict()
    del staff['id']

    query = insert(db.staff)
    result = await db.database.execute(query, staff)
    return result


@post_router.post("/place/")
async def create_place(place: pydantic_models.Places):
    place = place.dict()
    del place['id']

    query = insert(db.places)
    result = await db.database.execute(query, place)
    return result


@post_router.post("/adv/")
async def create_adv(adv: pydantic_models.Advertisements):
    adv = adv.dict()
    del adv['id']

    query = insert(db.advertisements)
    result = await db.database.execute(query, adv)
    return result


@post_router.post("/user/")
async def create_user(user: pydantic_models.Users):
    user = user.dict()
    del user['id']

    query = insert(db.users)
    result = await db.database.execute(query, user)
    return result


@post_router.post("/course/")
async def create_course(course: pydantic_models.Courses):
    course = course.dict()
    del course['id']

    query = insert(db.courses)
    result = await db.database.execute(query, course)
    return result


@post_router.post("/dogcourse/")
async def create_dogcourse(dogcourse: pydantic_models.DogCourse):
    dogcourse = dogcourse.dict()
    del dogcourse['id']

    query = insert(db.dogCourse)
    result = await db.database.execute(query, dogcourse)
    return result


@post_router.post("/session/")
async def create_session(session: pydantic_models.Sessions):
    session = session.dict()
    del session['id']

    query = insert(db.sessions)
    result = await db.database.execute(query, session)
    return result