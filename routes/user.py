from fastapi import APIRouter
from config.db import conn, session
from models.user import users
from schemas.user import User

user_route = APIRouter()


@user_route.get("/")
async def read_data():
    data = session.query(users).all()
    return data
    # return conn.execute(users.select()).fetchall()


@user_route.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user_route.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    conn.commit()
    return conn.execute(users.select()).fetchall()


@user_route.put("/{id}")
async def update_data(id:int,user: User):
    conn.execute(users.update(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


@user_route.delete("/")
async def delete_data():
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

