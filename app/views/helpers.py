from datetime import datetime
from app import parse_config_vars

def pay_period_helper(start_date_obj, end_date_obj):
    required_date_formats = parse_config_vars.get_required_date_formats()
    view_format = required_date_formats['view']

    pay_period_start = datetime.strftime(start_date_obj, view_format)
    pay_period_end = datetime.strftime(end_date_obj, view_format)
    pay_period = '{} - {}'.format(pay_period_start, pay_period_end)

    return pay_period

def kwargs_edit_helper(kwargs_to_edit, pay_period):
    kwargs_to_edit.pop('start_date_obj')
    kwargs_to_edit.pop('end_date_obj')
    kwargs_to_edit['pay_period'] = pay_period

    first_name = kwargs_to_edit['first_name']
    last_name = kwargs_to_edit['last_name']
    formatted_name = '{} {}'.format(first_name, last_name)

    kwargs_to_edit.pop('first_name')
    kwargs_to_edit.pop('last_name')
    kwargs_to_edit['name'] = formatted_name

    return kwargs_to_edit
