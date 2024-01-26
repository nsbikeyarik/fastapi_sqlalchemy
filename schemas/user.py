from pydantic import BaseModel


class UserModelRequest(BaseModel):
    name: str
    email: str
    password: str
