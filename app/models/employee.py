from sqlalchemy import Column, Integer, String, Float
from app.models import db_connector

class Employee(db_connector.Base, db_connector.DBConnector):
    __tablename__ = 'employee'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    annual_salary = Column(Integer)
    superannuation_rate = Column(Float)

    @classmethod
    def get_by_name(cls, first, last):
        session = cls.get_session()
        records = session.query(cls).filter_by(first_name=first,
                                               last_name=last).all()
        return records

    @classmethod
    def get_by_id(cls, id_number):
        session = cls.get_session()
        record = session.query(cls).filter_by(id=id_number).first()
        return record
