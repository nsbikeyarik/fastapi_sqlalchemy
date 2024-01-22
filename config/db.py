from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

engine = create_engine("postgresql://postgres:password@127.0.0.1:5432")


def get_session():
    return Session(engine)
