import unittest
import mock
from datetime import datetime

from app.views import helpers

class TestViewHelpers(unittest.TestCase):


    @mock.patch('app.parse_config_vars')
    def test_pay_period_helper(self, mock_parse_config_vars):

        mock_parse_config_vars.get_required_date_formats.return_value = {
            'views': '%d %B'
        }

        expected_result = '01 June - 30 June'

        start_date_obj = datetime.strptime('01-06-2010', '%d-%m-%Y')
        end_date_obj = datetime.strptime('30-06-2010', '%d-%m-%Y')

        result = helpers.pay_period_helper(start_date_obj, end_date_obj)

        self.assertEquals(result, expected_result)


    def test_kwargs_edit_helper(self):

        start_date_obj = datetime.strptime('01-05-2012', '%d-%m-%Y')
        end_date_obj = datetime.strptime('31-05-2012', '%d-%m-%Y')

        kwargs_to_edit = {
            'first_name':'Bob',
            'last_name':'James',
            'start_date_obj':start_date_obj,
            'end_date_obj':end_date_obj,
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

        pay_period = '01 May - 31 May'

        result = helpers.kwargs_edit_helper(kwargs_to_edit, pay_period)
        self.assertEquals(result, expected_result)




