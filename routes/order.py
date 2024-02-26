from fastapi import APIRouter
from config.db import get_session

from database_models import Order
from exceptions import UserNotExists, OrderNotExists
from routes.user import get_user_by_id
from schemas.user import OrderModelRequest
from sqlalchemy import select, update, insert, delete
from database_models import User

order_route = APIRouter()


@order_route.get("/")
def read_order():
    with get_session() as session:
        query = (select(Order))
        return session.execute(query).scalars().all()


@order_route.get("/{id}")
async def read_order(user_id: int):
    order = get_order_by_id(user_id)
    if order:
        return order
    else:
        raise OrderNotExists(f"No such Order with id {user_id}")


@order_route.post("/")
async def write_order(order: OrderModelRequest):
    with get_session() as session:
        if get_user_by_id(order.user_id):
            query = (
                insert(Order).values(
                    item=order.item,
                    price=order.price,
                    date=order.date,
                    user_id=order.user_id
                )
            )
            session.execute(query)
            session.commit()
            return session.execute(select(Order)).scalars().all()
        else:
            raise UserNotExists(f"No such User with id {order.user_id}")


@order_route.put("/{id}")
async def update_order(user_id: int, order: OrderModelRequest):
    with get_session() as session:
        query = (
            update(Order).values(
                item=order.item,
                price=order.price,
                date=order.date,
                user_id=order.user_id
            )
        ).where(Order.id == user_id)
        session.execute(query)
        session.commit()
        return session.execute(select(Order)).scalars()


@order_route.delete("/")
async def delete_order(user_id: int):
    with get_session() as session:
        query = (
            delete(Order).where(Order.id == user_id)
        )
        session.execute(query)
        session.commit()


def get_order_by_id(user_id):
    with get_session() as session:
        query = (select(Order).where(Order.id == user_id).limit(1))
        user_info = session.execute(query)
        return user_info.scalars().first()