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
    def filter_employee_ids(cls, all_records):
        id_numbers = []
        for employee in all_records:
            id_numbers.append(employee.id)
        return id_numbers

    @classmethod
    def get_by_name(cls, first, last):
        session = cls.get_session()
        all_records = session.query(cls).filter_by(first_name=first,
                                                   last_name=last).all()
        if len(all_records) < 1:
            err_message = """There is no database record of an employee called
            {} {}.""".format(first, last)
            raise IndexError(err_message)
        elif len(all_records) > 1:
            id_numbers = cls.filter_employee_ids(all_records)
            err_message = """There is more than one employee called {} {}. Try
            retrieving the record with --employee_id NUMBER. Valid employee_id
            numbers are {}""".format(first, last, id_numbers)
            raise IndexError(err_message)

        one_record = all_records[0]
        return one_record

    @classmethod
    def get_by_id(cls, id_number):
        session = cls.get_session()
        all_records = session.query(cls).filter_by(id=id_number).all()

        if len(all_records) < 1:
            err_message = """There is no database record of an employee with
            id number {}.""".format(id_number)
            raise IndexError(err_message)

        one_record = all_records[0]
        return one_record

