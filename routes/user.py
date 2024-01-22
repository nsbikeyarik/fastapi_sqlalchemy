from fastapi import APIRouter
from config.db import get_session

from database_models import User
from schemas.user import UserModel
from sqlalchemy import select, update, insert

user_route = APIRouter()


@user_route.get("/")
def read_data():
    with get_session() as session:
        query = (select(User))
        return session.execute(query).scalars().all()


@user_route.get("/{id}")
async def read_data(user_id: int):
    with get_session() as session:
        query = (select(User).where(User.id == user_id).limit(1))
        user_info = session.execute(query)
        return user_info.scalars().first()


@user_route.post("/")
async def write_data(user: UserModel):
    with get_session() as session:
        query = (
            insert(User).values(
                name=user.name,
                email=user.email,
                password=user.password
            )
        )
        session.execute(query)
        session.commit()
        return session.execute(select(User)).scalars().all()


# @user_route.put("/{id}")
# async def update_data(user_id: int, user: User):
#     conn.execute(users.update().values(
#         name=user.name,
#         email=user.email,
#         password=user.password
#     ).where(users.c.id == user_id))
#     data = conn.execute(users.select()).fetchall()
#     return [tuple(row) for row in data]


# @user_route.delete("/")
# async def delete_data():
#     conn.execute(users.delete().where(users.c.id == id))
#     data = conn.execute(users.select()).fetchall()
#     return [tuple(row) for row in data]

