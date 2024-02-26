from pydantic import BaseModel




class UserModelRequest(BaseModel):
    name: str
    email: str
    password: str


class OrderModelRequest(BaseModel):
    user_id: int
    item: str
    price: str
    date: str


