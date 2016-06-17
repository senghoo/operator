import logging
from sqlalchemy import create_engine, Column, String, Integer, DateTime,\
    ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///db.sqlite")
session_factory = sessionmaker(bind=engine, autocommit=False,
                               autoflush=True, expire_on_commit=False)
Session = scoped_session(session_factory)


logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


class TextMessage(Base):
    __tablename__ = 'text_messages'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    sender = Column(String(64))
    content = Column(String(512))
    time = Column(DateTime)

    @classmethod
    def get_all(cls):
        return Session().query(cls).all()

    @classmethod
    def save_sms(cls, sms):
        n = TextMessage(sender=sms.number, content=sms.text, time=sms.time)
        session = Session()
        session.add(n)
        session.commit()


Base.metadata.create_all(engine)

