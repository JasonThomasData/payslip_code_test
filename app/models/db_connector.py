import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DBConnector():
    '''
    where every row is the details one employee was paid for an entire month.
    '''

    @classmethod
    def get_session(cls):

        database_path = os.environ["SQL_DATABASE"]

        engine = create_engine(database_path)
        session = sessionmaker(bind=engine)()
        return session
