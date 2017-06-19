import unittest
import mock
from app.controllers.concerns import payg_calculation, date_parse

class TestPAYGCalculateConcern(unittest.TestCase):

    mock_tax_rates = [
        {
            "range": {
                "minimum": 0,
                "maximum": 18200
            },
            "base": 0,
            "extra": {
                "threshold": 0,
                "rate": 0
            }
        },
        {
            "range": {
                "minimum": 18201,
                "maximum": 37000
            },
            "base": 0,
            "extra": {
                "threshold": 18200,
                "rate": 0.19
            }
        },
        {
            "range": {
                "minimum": 37001,
                "maximum": 80000
            },
            "base": 3572,
            "extra": {
                "threshold": 37000,
                "rate": 0.325
            }
        },
        {
            "range": {
                "minimum": 80001,
                "maximum": 180000
            },
            "base": 17547,
            "extra": {
                "threshold": 80000,
                "rate": 0.37
            }
        },
        {
            "range": {
                "minimum": 180001
            },
            "base": 54547,
            "extra": {
                "threshold": 180000,
                "rate": 0.45
            }
        }
    ]

    def test_get_monthly_gross_income(self):
        '''
        65,000/12 = 5416.666666667. Make sure this rounds down.
        '''
        annual_salary = 65000

        result = payg_calculation.get_monthly_gross_income(annual_salary)
        expected_result = 5416

        self.assertEquals(result, expected_result)

    def test_get_monthly_net_income(self):
        gross_income = 4010
        income_tax = 900

        result = payg_calculation.get_monthly_net_income(gross_income, income_tax)
        expected_result = 3110

        self.assertEquals(result, expected_result)

    def test_get_montly_income_tax_1(self):
        '''
        A person's tax rate, for an annual salary of 64000, is equal to:
        (3572 + (.325 * (64000 - 37000)) / 12) = 1028.916666667
        Rounded up = 1029
        '''

        annual_salary = 64000
        tax_bracket = {
            "range": {
                "minimum": 37001,
                "maximum": 80000
            },
            "base": 3572,
            "extra": {
                "threshold": 37000,
                "rate": 0.325
            }
        }

        result = payg_calculation.get_monthly_income_tax(annual_salary, tax_bracket)
        expected_result = 1029

        self.assertEquals(result, expected_result)

    def test_get_montly_income_tax_2(self):
        '''
        A person's tax rate, for an annual salary of 64000, is equal to:
        (0 + (.19 * (21000 - 18201)) / 12) = 44.3175
        Rounded up = 45
        '''

        annual_salary = 21000
        tax_bracket = {
            "range": {
                "minimum": 18201,
                "maximum": 37000
            },
            "base": 0,
            "extra": {
                "threshold": 18200,
                "rate": 0.19
            }
        }

        result = payg_calculation.get_monthly_income_tax(annual_salary, tax_bracket)
        expected_result = 45

        self.assertEquals(result, expected_result)

    @mock.patch('app.parse_config_vars.get_tax_brackets')
    def test_get_tax_bracket_1(self, mock_get_tax_brackets):
        '''
        A person with an annual salary of 60010.10 has a rounded down annual
        salary of 60010.10. That person falls in the 37001-80000 tax
        bracket
        '''

        mock_get_tax_brackets.return_value = self.mock_tax_rates 

        annual_salary = 60010.10

        tax_bracket = payg_calculation.get_tax_bracket(annual_salary)
        bracket_base_tax = tax_bracket['base']
        expected_base_tax = 3572

        self.assertEquals(bracket_base_tax, expected_base_tax)

    @mock.patch('app.parse_config_vars.get_tax_brackets')
    def test_get_tax_bracket_2(self, mock_get_tax_brackets):
        '''
        A person with an annual salary of 60010.10 has a rounded down annual
        salary of 290000. That person falls in the 180000+ tax bracket
        '''

        mock_get_tax_brackets.return_value = self.mock_tax_rates 

        annual_salary = 290000

        tax_bracket = payg_calculation.get_tax_bracket(annual_salary)
        bracket_base_tax = tax_bracket['base']
        expected_base_tax = 54547

        self.assertEquals(bracket_base_tax, expected_base_tax)


class TestDateParse(unittest.TestCase):

    @mock.patch('app.parse_config_vars.get_required_date_formats')
    def test_get_pay_period(self, mock_get_date_formats):
        '''
        Function raises error if there's an issue, should be no issue.
        '''

        mock_get_date_formats.return_value = {
            'input': '%d-%m-%Y'
        }

        start_date = '01-01-2000'
        end_date = '31-01-2000'

        date_parse.get_pay_period(start_date)

    @mock.patch('app.parse_config_vars.get_required_date_formats')
    def test_get_pay_period_fail_1(self, mock_get_date_formats):
        '''
        Fails because dates are required to be zero padded, like 01-01
        '''

        mock_get_date_formats.return_value = {
            'input': '%d-%m-%Y'
        }

        start_date = '1-Jan-2000'
        end_date = '31-1-2000'
        
        with self.assertRaises(Exception) as test_fail:
            date_parse.get_pay_period(start_date)
