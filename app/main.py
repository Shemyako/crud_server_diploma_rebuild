from fastapi import FastAPI, Depends, HTTPException

import db
from .router.post import post_router
from .router.get import get_router
from .router.put import put_router


# Мб эту функцию потом под авторизацию подогнать
async def wrapper():
    print("Ola")
    # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


app = FastAPI(dependencies=[Depends(wrapper)])


@app.on_event("startup")
async def startup():
    '''
    Открытие соединения с бд при запуске сервера
    '''
    await db.database.connect()


@app.on_event("shutdown")
async def shutdown():
    '''
    Закрытие соединения с бд при остановке сервера
    '''
    await db.database.disconnect()


app.include_router(post_router)
app.include_router(get_router)
app.include_router(put_router)