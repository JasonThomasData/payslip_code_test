from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class DBConnector():
    '''
    where every row is the details one employee was paid for an entire month.
    '''

    @classmethod
    def get_session(self):

        database_path = os.environ["DATABASE"]

        engine = create_engine(database_path)
        session = sessionmaker(bind=engine)()
        return session