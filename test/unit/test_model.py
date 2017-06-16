import sys
import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append('/home/john/programming/python/payslips_test/app')
from app.models import employee, db_connector

# Test the model at app/model/employee.py

class TestEmployeeModel(unittest.TestCase):

    test_db_path = 'test/test.db'
    sqlite_db = 'sqlite:///test/test.db'

    def setUp(self):
        os.environ["DATABASE"] = self.sqlite_db

        engine = create_engine(self.sqlite_db)
        employee.Employee.metadata.create_all(engine)

        session = sessionmaker(bind=engine)()
        employee_data = {
            "first_name": "John",
            "last_name": "Smith",
            "annual_salary": 60500,
            "superannuation_rate": 9.5
        }
        new_employee = employee.Employee(**employee_data)
        session.add(new_employee)
        session.commit()

    def test_retrieve_employee_by_name(self):
        employees = employee.Employee.get_by_name("John", "Smith")

        first_name = employees[0].first_name
        salary = employees[0].annual_salary

        expected_first_name = 'John'
        expected_salary = 60500

        self.assertEquals(first_name, expected_first_name)
        self.assertEquals(salary, expected_salary)

    def test_retrieve_employee_by_id(self):
        '''
        The employee is the first added and will have an id=1.
        '''
        employees = employee.Employee.get_by_id(1)

        first_name = employees[0].first_name
        salary = employees[0].annual_salary

        expected_first_name = 'John'
        expected_salary = 60500

        self.assertEquals(first_name, expected_first_name)
        self.assertEquals(salary, expected_salary)

    def tearDown(self):
        os.remove(self.test_db_path)
