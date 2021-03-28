from datetime import datetime

from src.db.init_db import init_db
from src.db.session import db_session
from src.db.base import Base
from sqlalchemy import Column, Integer, String, Date


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)

    def __init__(self, first_name, middle_name, last_name, date_of_birth):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


init_db(db_session)

def add_new_user(db_session):
    user = User('Test', 'User', '-', datetime(1990, 1, 1))
    try:
        db_session.add(user)
        db_session.commit()
        return True
    except Exception:
        return False


status = add_new_user(db_session)
print(status)
