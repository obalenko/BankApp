from src.db.base import Base
from src.db.session import engine


def init_db(db_session):
    """
    Database initialization.
    :param db_session:
    :return:
    """
    Base.metadata.create_all(bind=engine)
