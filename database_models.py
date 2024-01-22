from sqlalchemy import MetaData
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, Mapped, mapped_column


class Base(MappedAsDataclass, DeclarativeBase):
    metadata = MetaData()


metadata = Base.metadata


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
