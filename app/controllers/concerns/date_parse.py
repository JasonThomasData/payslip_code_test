from datetime import datetime
from dateutil.relativedelta import relativedelta
from app import parse_config_vars

def get_pay_period_last_day(start_date_obj):
    end_date_obj = (start_date_obj +
                    relativedelta(months=1) -
                    relativedelta(days=1) )

    return end_date_obj

def get_pay_period(start_date):
    required_date_formats = parse_config_vars.get_required_date_formats()
    input_format = required_date_formats['input']

    try:
        start_date_obj = datetime.strptime(start_date, input_format)
    except ValueError:
        err_message = 'The required format for dates is {}, like 01-01-2000'
        err_message.format(input_format)
        raise Exception(err_message)

    end_date_obj = get_pay_period_last_day(start_date_obj)

    return start_date_obj, end_date_obj
