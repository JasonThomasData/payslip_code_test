import os
import sys
import yaml
import unittest
from sqlalchemy import create_engine

# Test the CLI at app/seed.py

import seed
from app.models import employee

class TestSeedData(unittest.TestCase):

    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file)
        test_db_path = config_data['data_paths']['test']['database_path']
        sqlite_db = config_data['data_paths']['test']['sql_path']
        os.environ['SQL_DATABASE'] = sqlite_db

    def setUp(self):

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
    
    def test_parse_csv(self):

        with open('config.yml', 'r') as config_file:
            config_data = yaml.load(config_file)
            seed_path = config_data['data_paths']['test']['seed_path']

        parsed_seed_data = seed.parse_csv(seed_path)

        expected_seed_data = [{
            'first_name': 'Jack',
            'last_name': 'Skinner',
            'annual_salary': '60500',
            'superannuation_rate': '9.5'
        }]
        
        self.assertEquals(parsed_seed_data, expected_seed_data)

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
