from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from models import db_connector

class Employee(db_connector.Base, db_connector.DBConnector):
    '''
    Where every row is the details one employee was paid for an entire month.
    There would be an authoritative Employee database with unique IDs already.
    '''
    __tablename__ = 'monthly_salary'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False) #required=True
    last_name = Column(String(100), nullable=False) #required=True
    annual_salary = Column(Integer) #required=True
    superannuation_rate = Column(Float) #required=True

    @classmethod
    def get_by_name(self, first, last):
        session = self.get_session()
        records = session.query(self).filter_by(first_name=first,
             last_name=last).all()
        return records

    @classmethod
    def get_by_id(self, id_number):
        session = self.get_session()
        record = session.query(self).filter_by(id=id_number).first()
        return record
