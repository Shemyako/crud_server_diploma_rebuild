from fastapi import APIRouter
from sqlalchemy import update
# from models import *
from . import pydantic_models
import db


put_router = APIRouter()  


@put_router.put("/type_of_lesson/")
async def edit_type_of_lesson(type_of_lesson: pydantic_models.TypesOfLesson):
    # type_of_lesson.dict() - values to insert
    type_of_lesson = type_of_lesson.dict()

    # update table, where id == our id
    query = update(db.typesOfLesson).where(db.typesOfLesson.c.id == type_of_lesson['id'])
    result = await db.database.execute(query, type_of_lesson)
    return result


@put_router.put("/dog/")
async def edit_dog(dog: pydantic_models.Dogs):
    dog = dog.dict()

    query = update(db.dogs).where(db.dogs.c.id == dog['id'])
    result = await db.database.execute(query, dog)
    return result


@put_router.put("/userdog/")
async def edit_userdog(userdog: pydantic_models.UserDog):
    userdog = userdog.dict()

    query = update(db.userDog).where(db.userDog.c.id == userdog['id'])
    result = await db.database.execute(query, userdog)
    return result


@put_router.put("/lesson/")
async def edit_lesson(lesson: pydantic_models.Lessons):
    lesson = lesson.dict()

    query = update(db.lessons).where(db.lessons.c.id == lesson['id'])
    result = await db.database.execute(query, lesson)
    return result


@put_router.put("/staff/")
async def edit_staff(staff: pydantic_models.Staff):
    staff = staff.dict()

    query = update(db.staff).where(db.staff.c.id == staff['id'])
    result = await db.database.execute(query, staff)
    return result


@put_router.put("/place/")
async def edit_place(place: pydantic_models.Places):
    place = place.dict()

    query = update(db.places).where(db.places.c.id == place['id'])
    result = await db.database.execute(query, place)
    return result


@put_router.put("/adv/")
async def edit_adv(adv: pydantic_models.Advertisements):
    adv = adv.dict()

    query = update(db.advertisements).where(db.advertisements.c.id == adv['id'])
    result = await db.database.execute(query, adv)
    return result


@put_router.put("/user/")
async def edit_user(user: pydantic_models.Users):
    user = user.dict()

    query = update(db.users).where(db.users.c.id == user['id'])
    result = await db.database.execute(query, user)
    return result


@put_router.put("/course/")
async def edit_course(course: pydantic_models.Courses):
    course = course.dict()

    query = update(db.courses).where(db.courses.c.id == course['id'])
    result = await db.database.execute(query, course)
    return result


@put_router.put("/dogcourse/")
async def edit_dogcourse(dogcourse: pydantic_models.DogCourse):
    dogcourse = dogcourse.dict()

    query = update(db.dogCourse).where(db.dogCourse.c.id == dogcourse['id'])
    result = await db.database.execute(query, dogcourse)
    return result


@put_router.put("/session/")
async def edit_session(session: pydantic_models.Sessions):
    session = session.dict()

    query = update(db.sessions).where(db.sessions.c.id == session['id'])
    result = await db.database.execute(query, session)
    return result