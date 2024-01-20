from fastapi import APIRouter
from config.db import conn, session
from models.user import users
from schemas.user import User
from sqlalchemy import select

user_route = APIRouter()


@user_route.get("/")
def read_data():
    query = select(users)
    data = session.execute(query).all()
    data = [tuple(row) for row in data]
    return data


@user_route.get("/{id}")
async def read_data(user_id: int):
    query = select(users).where(users.c.id == user_id)
    data = conn.execute(query).fetchall()
    return [tuple(row) for row in data]


@user_route.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    conn.commit()
    data = conn.execute(users.select()).fetchall()
    return [tuple(row) for row in data]


@user_route.put("/{id}")
async def update_data(user_id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == user_id))
    data = conn.execute(users.select()).fetchall()
    return [tuple(row) for row in data]


@user_route.delete("/")
async def delete_data():
    conn.execute(users.delete().where(users.c.id == id))
    data = conn.execute(users.select()).fetchall()
    return [tuple(row) for row in data]

