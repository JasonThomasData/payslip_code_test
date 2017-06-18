import os
import sys
import unittest
from sqlalchemy import create_engine

# Test the CLI at app/seed.py

sys.path.append('/home/john/programming/python/payslips_test/app')
from app import seed
from app.models import employee

class TestSeedParseCsv(unittest.TestCase):

    def test_parse_csv(self):

        os.environ['SEED_DATA'] = 'test/data/seed_data.csv'

        parsed_seed_data = seed.parse_csv()

        expected_seed_data = [{
            'first_name': 'Jack',
            'last_name': 'Skinner',
            'annual_salary': '60500',
            'superannuation_rate': '9.5'
        }]
        
        self.assertEquals(parsed_seed_data, expected_seed_data)

class TestSeedData(unittest.TestCase):

    test_db_path = 'test/data/test.db'
    sqlite_db = 'sqlite:///test/data/test.db'

    def setUp(self):
    
        employee.Employee.__table_args__ = {'extend_existing': True}

        os.environ["DATABASE"] = self.sqlite_db

        engine = create_engine(self.sqlite_db)
        employee.Employee.metadata.create_all(engine)

        seed_data = [
            {
                'first_name': 'Jack',
                'last_name': 'Skinner',
                'annual_salary': '60500',
                'superannuation_rate': '9.5'
            },
            {
                'first_name': 'Sarah',
                'last_name': 'Warner',
                'annual_salary': '70500',
                'superannuation_rate': '8.5'
            }
        ]

        seed.seed_database(engine, seed_data)

    def test_create_db_from_csv_1(self):
        all_employees = employee.Employee.get_by_name("Jack", "Skinner")

        first_name = all_employees[0].first_name
        salary = all_employees[0].annual_salary

        expected_first_name = 'Jack'
        expected_salary = 60500

        self.assertEquals(first_name, expected_first_name)
        self.assertEquals(salary, expected_salary)

    def test_create_db_from_csv_2(self):
        all_employees = employee.Employee.get_by_name("Sarah", "Warner")

        first_name = all_employees[0].first_name
        salary = all_employees[0].annual_salary

        expected_first_name = 'Sarah'
        expected_salary = 70500

        self.assertEquals(first_name, expected_first_name)
        self.assertEquals(salary, expected_salary)

    def tearDown(self):
        os.remove(self.test_db_path)
