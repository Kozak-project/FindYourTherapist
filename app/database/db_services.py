import logging
from app.database.database import SessionLocal
from app.database.models import User, Message
from sqlalchemy.exc import SQLAlchemyError


def save_user(user: User):
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    is_bot = user.is_bot
    language_code = user.language_code

    session = SessionLocal()
    try:
        is_user = session.query(User).filter(User.id == user.id).first()

        if not is_user:
            new_user = User(id=user_id, first_name=first_name, last_name=last_name,
                            username=username, is_bot=is_bot,
                            language_code=language_code)
            session.add(new_user)
            session.commit()
    except SQLAlchemyError as e:
        logging.error(f'SQLAlchemy error: {e}')
        session.rollback()
    finally:
        session.close()


def save_message(message: Message, user: User):
    message_id = message.message_id
    message_text = message.text
    message_date = message.date
    user_id = user.id

    session = SessionLocal()
    try:
        if user.is_bot:
            new_message = Message(message_id=None, text=message_text, date=message_date, user_id=user_id, role='assistant')
        else:
            new_message = Message(message_id=message_id, text=message_text, date=message_date, user_id=user_id, role='user')
        session.add(new_message)
        session.commit()
    except SQLAlchemyError as e:
        logging.error(f'SQLAlchemy error: {e}')
        session.rollback()
    finally:
        session.close()