import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

SQLALCHEMY_DATABASE_URI = 'secret'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

try:
    engine.connect()
except Exception:
    print('Database connection error')
    sys.exit()


db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)