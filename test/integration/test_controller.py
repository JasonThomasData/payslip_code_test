import os
import unittest
import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import employee
from app.controllers import payslip

# test the file at app/controllers/payslip.py

class TestPayslipsController(unittest.TestCase):
    
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

    def test_controller_1(self):
        parsed_args = {
            'first_name': 'Sally',
            'last_name': 'Watson',
            'start_date': '01-01-2010'
        }

        result = payslip.one_employee(**parsed_args)
        assert '| 01 January - 31 January' in result
        assert '| Sally Watson' in result
        assert 'Gross income | 6708' in result

    def test_controller_2(self):
        parsed_args = {
            'first_name': 'John',
            'last_name': 'Smith',
            'start_date': '01-07-2010',
            'id': 1
        }

        result = payslip.one_employee(**parsed_args)
        assert '| 01 July - 31 July' in result
        assert '| John Smith' in result

    def test_controller_fail_1(self):
        parsed_args = {
            'first_name': 'Not a',
            'last_name': 'real person',
            'start_date': '01-01-2010'
        }

        with self.assertRaises(Exception) as test_fail:
            result = payslip.one_employee(**parsed_args)

    def test_controller_fail_2(self):
        '''
        Fails because the date is not correctly formatted, see config.yml
        '''
        parsed_args = {
            'first_name': 'Sally',
            'last_name': 'Watson',
            'start_date': '01-Jan-2010'
        }

        with self.assertRaises(Exception) as test_fail:
            result = payslip.one_employee(**parsed_args)

    def tearDown(self):
        os.remove(self.test_db_path)
