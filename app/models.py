from sqlalchemy import String, Column, Integer, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=True)
    username = Column(String(45), nullable=True)
    is_bot = Column(Boolean, nullable=False)
    language_code = Column(String(45), nullable=True)


class Conversation(Base):
    pass


class Message(Base):
    pass