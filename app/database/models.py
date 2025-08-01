from sqlalchemy import String, Column, Integer, Boolean, ForeignKey, DateTime, Text, BigInteger
from sqlalchemy.orm import relationship
from app.database.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=True)
    username = Column(String(45), nullable=True)
    is_bot = Column(Boolean, nullable=False)
    language_code = Column(String(45), nullable=True)

    messages = relationship('Message', back_populates='user')


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, nullable=False)
    text = Column(Text, nullable=True)
    date = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='messages')
