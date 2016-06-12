from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from utils import make_path

db_path = make_path("db.sqlite")

Base = declarative_base()
engine = create_engine("sqlite://{0}".format(db_path))


class TextMessage(Base):
    __tablename__ = 'text_messages'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    sender = Column(String(64))
    content = Column(String(512))
