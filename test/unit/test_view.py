import unittest
import mock
import json

from app.views import payslip_view

# test the file at app/views/payslip_view.py

class TestPayslipsViewHelpers(unittest.TestCase):

    @mock.patch('app.parse_config_vars')
    def test_pay_period_helper(self, mock_parse_config_vars):

        mock_parse_config_vars.get_required_date_formats.return_value = {
            'input': '%d-%m-%y',
            'views': '%d %B'
        }

        expected_result = '01 June - 30 June'

        start_date = '01-06-2010'
        end_date = '30-06-2010'

        result = payslip_view.pay_period_helper(start_date, end_date)

        self.assertEquals(result, expected_result)

    @mock.patch('app.views.payslip_view.pay_period_helper')
    def test_kwargs_edit_helper(self, mock_pay_period_helper):

        mock_pay_period_helper.return_value = '01 May - 31 May'

        kwargs_to_edit = {
            'first_name':'Bob',
            'last_name':'James',
            'start_date':'01-05-2012',
            'end_date':'31-05-2012',
            'gross_income':5000,
            'income_tax':900,
            'net_income':4100,
            'superannuation':800
        }

        expected_result = {
            'name':'Bob James',
            'pay_period':'01 May - 31 May',
            'gross_income':5000,
            'income_tax':900,
            'net_income':4100,
            'superannuation':800
        }

        result = payslip_view.kwargs_edit_helper(kwargs_to_edit)
        self.assertEquals(result, expected_result)

class TestPayslipView(unittest.TestCase):
    
    @mock.patch('app.parse_config_vars')
    def test_as_json(self, mock_parse_config_vars):

        mock_parse_config_vars.get_required_date_formats.return_value = {
            'input': '%d-%m-%y',
            'views': '%d %B'
        }

        expected_dict = {
            'Name': 'Bob James',
            'Pay period': '01 May - 31 May',
            'Gross income': 5000,
            'Income tax': 900,
            'Net income': 4100,
            'Super': 800
        }
        expected_result = json.dumps(expected_dict)

        result = payslip_view.as_json(first_name='Bob', last_name='James',
            start_date='01-05-2012', end_date='31-05-2012', gross_income=5000,
            income_tax=900, net_income=4100, superannuation=800)

        self.assertEquals(result, expected_result)

    @mock.patch('app.parse_config_vars')
    def test_as_blob(self, mock_parse_config_vars):
        '''
        Test will strip both strings of their extra spaces so they can
        accurately compared.
        '''

        mock_parse_config_vars.get_required_date_formats.return_value = {
            'input': '%d-%m-%y',
            'views': '%d %B'
        }

        test_data = {
            'first_name': 'Mary',
            'last_name': 'Jacobs',
            'start_date': '01-03-2014',
            'end_date': '31-03-2014',
            'gross_income': 4000,
            'income_tax': 800,
            'net_income': 3200,
            'superannuation': 700
        }

        expected_result = '''
        Name         | Mary Jacobs
        Pay period   | 01 March - 31 March
        Gross income | 4000
        Income tax   | 800
        Net income   | 3200
        Super        | 700
        '''
        stripped_expected_result = ' '.join(expected_result.split())

        result = payslip_view.as_blob(first_name='Mary', last_name='Jacobs',
            start_date='01-03-2014', end_date='31-03-2014', gross_income=4000,
            income_tax=800, net_income=3200, superannuation=700)
        stripped_result = ' '.join(result.split())

        self.assertEquals(stripped_result, stripped_expected_result)

