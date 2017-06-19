import sys
import yaml
import unittest
import importlib

# Test the CLI at app/payslips.py

import payslips

class TestPayslipsCLI(unittest.TestCase):

    def test_parse_arguments_1(self):
        arguments = ['./payslips', '--first_name', 'Jack', '--last_name',
            'Skinner', '--start_date', '1-2-2000', '--end_date', '2-2-2000']

        required_args = ['first_name', 'last_name', 'start_date', 'end_date']
        optional_args = ['id']
        allowed_args = required_args + optional_args

        parsed_args = payslips.parse_arguments(allowed_args, arguments)

        expected_parsed_args = {
            'first_name': 'Jack',
            'last_name': 'Skinner',
            'start_date': '1-2-2000',
            'end_date': '2-2-2000'
        }

        self.assertEquals(parsed_args, expected_parsed_args)

    def test_parse_arguments_2(self):
        arguments = ['./payslips', '--first_name', 'Jack', '--last_name',
            'Skinner', '--start_date', '1-2-2000', '--end_date', '2-2-2000',
            'id', '1']

        required_args = ['first_name', 'last_name', 'start_date', 'end_date']
        optional_args = ['id']
        allowed_args = required_args + optional_args

        parsed_args = payslips.parse_arguments(allowed_args, arguments)

        expected_parsed_args = {
            'first_name': 'Jack',
            'last_name': 'Skinner',
            'start_date': '1-2-2000',
            'end_date': '2-2-2000',
            'id': '1'
        }

        self.assertEquals(parsed_args, expected_parsed_args)

    def test_check_arguments(self):

        parsed_args = {
            'first_name': 'Jack',
            'last_name': 'Skinner',
            'start_date': '1-2-2000',
            'end_date': '2-2-2000'
        }

        required_args = ['first_name', 'last_name', 'start_date', 'end_date']

        payslips.check_required_arguments(required_args, parsed_args)

    def test_check_arguments_fail(self):

        parsed_args = {
            'first_name': 'Jack',
            'last_name': 'Skinner',
            'start_date': '1-2-2000',
            'id': '1'
        }

        required_args = ['first_name', 'last_name', 'start_date', 'end_date']
 
        with self.assertRaises(Exception) as test_fail:
            payslips.check_required_arguments(required_args, parsed_args)

