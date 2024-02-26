from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, Mapped, mapped_column, relationship


class Base(MappedAsDataclass, DeclarativeBase):
    metadata = MetaData()


metadata = Base.metadata


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey('users.id'), nullable=False)
    item: Mapped[str]
    price: Mapped[int]
    date: Mapped[str]

