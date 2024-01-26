from fastapi import APIRouter
from config.db import get_session

from database_models import User
from schemas.user import UserModelRequest
from sqlalchemy import select, update, insert, delete

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
async def write_data(user: UserModelRequest):
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


@user_route.put("/{id}")
async def update_data(user_id: int, user: UserModelRequest):
    with get_session() as session:
        query = (
            update(User).values(
                name=user.name,
                email=user.email,
                password=user.password
            )
        ).where(User.id == user_id)
        session.execute(query)
        session.commit()
        return session.execute(select(User)).scalars()


@user_route.delete("/")
async def delete_data(user_id: int):
    with get_session() as session:
        query = (
            delete(User).where(User.id == user_id)
        )
        session.execute(query)
        session.commit()



