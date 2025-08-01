from app.database.database import SessionLocal
from app.database.models import User, Message
from sqlalchemy.exc import SQLAlchemyError


def save_user(user):
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
    except SQLAlchemyError:
        session.rollback()
    finally:
        session.close()
