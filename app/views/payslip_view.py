import json
from datetime import datetime
from app import parse_config_vars

def pay_period_helper(start_date_obj, end_date_obj):
    required_date_formats = parse_config_vars.get_required_date_formats()
    view_format = required_date_formats['view']

    pay_period_start = datetime.strftime(start_date_obj, view_format)
    pay_period_end = datetime.strftime(end_date_obj, view_format)
    pay_period = '{} - {}'.format(pay_period_start, pay_period_end)

    return pay_period

def kwargs_edit_helper(kwargs_to_edit):

    first_name = kwargs_to_edit['first_name']
    last_name = kwargs_to_edit['last_name']
    formatted_name = '{} {}'.format(first_name, last_name)

    start_date_obj = kwargs_to_edit['start_date_obj']
    end_date_obj = kwargs_to_edit['end_date_obj']

    pay_period = pay_period_helper(start_date_obj, end_date_obj)
    kwargs_to_edit.pop('start_date_obj')
    kwargs_to_edit.pop('end_date_obj')
    kwargs_to_edit['pay_period'] = pay_period

    kwargs_to_edit.pop('first_name')
    kwargs_to_edit.pop('last_name')
    kwargs_to_edit['name'] = formatted_name

    return kwargs_to_edit

def as_json(**kwargs):

    kwargs = kwargs_edit_helper(kwargs)

    formatted_dict = {
        'Name': kwargs['name'],
        'Pay period': kwargs['pay_period'],
        'Gross income': kwargs['gross_income'],
        'Income tax': kwargs['income_tax'],
        'Net income': kwargs['net_income'],
        'Super': kwargs['superannuation']
    }
    json_data = json.dumps(formatted_dict)
    return json_data

def as_blob(**kwargs):

    kwargs = kwargs_edit_helper(kwargs)

    blob_template = '''
    Name         | {name}
    Pay period   | {pay_period}
    Gross income | {gross_income}
    Income tax   | {income_tax}
    Net income   | {net_income}
    Super        | {superannuation}
    '''
    blob = blob_template.format(**kwargs)
    return blob
