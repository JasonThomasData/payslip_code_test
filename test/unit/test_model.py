import sys
import os
import unittest
import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import employee, db_connector
from app import parse_config_vars

# Test the model at app/model/employee.py

class TestEmployeeModel(unittest.TestCase):

    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file)
        test_db_path = config_data['data_paths']['test']['database_path']
        sqlite_db = config_data['data_paths']['test']['sql_path']
        os.environ['SQL_DATABASE'] = sqlite_db

    def setUp(self):

        engine = create_engine(self.sqlite_db)
        employee.Employee.metadata.create_all(engine)

        session = sessionmaker(bind=engine)()
        all_employees_data = [
            {
                "first_name": "John",
                "last_name": "Smith",
                "annual_salary": 60500,
                "superannuation_rate": 9.5
            },
            {
                "first_name": "John",
                "last_name": "Smith",
                "annual_salary": 70500,
                "superannuation_rate": 8.5
            },
            {
                "first_name": "Sally",
                "last_name": "Watson",
                "annual_salary": 80500,
                "superannuation_rate": 7.5
            }
        ]
        for employee_data in all_employees_data:
            new_employee = employee.Employee(**employee_data)
            session.add(new_employee)
        session.commit()

    def test_retrieve_employee_by_name(self):
        all_employees = employee.Employee.get_by_name("Sally", "Watson")

        first_name = all_employees.first_name
        salary = all_employees.annual_salary

        expected_first_name = 'Sally'
        expected_salary = 80500

        self.assertEquals(first_name, expected_first_name)
        self.assertEquals(salary, expected_salary)

    def test_retrieve_employee_by_name_fail_1(self):
        with self.assertRaises(IndexError) as testfail:
            all_employees = employee.Employee.get_by_name("I Don't", "Exist")

    def test_retrieve_employee_by_name_fail_2(self):
        '''
        This fails because there are two in the db, so the user needs to
        get_by_id()
        '''
        with self.assertRaises(IndexError) as testfail:
            all_employees = employee.Employee.get_by_name("John", "Smith")

    def test_retrieve_employee_by_id(self):
        '''
        The employee is the first added and will have an id=1.
        '''
        one_employee = employee.Employee.get_by_id(1)

        first_name = one_employee.first_name
        salary = one_employee.annual_salary

        expected_first_name = 'John'
        expected_salary = 60500

        self.assertEquals(first_name, expected_first_name)
        self.assertEquals(salary, expected_salary)

    def test_retrieve_employee_by_id_fail(self):
        with self.assertRaises(IndexError) as testfail:
            all_employees = employee.Employee.get_by_id(20)

    def tearDown(self):
        os.remove(self.test_db_path)
