import json
from app import parse_config_vars
from app.views import helpers


def as_json(**kwargs):

    start_date_obj = kwargs['start_date_obj']
    end_date_obj = kwargs['end_date_obj']

    pay_period = helpers.pay_period_helper(start_date_obj, end_date_obj)
    kwargs = helpers.kwargs_edit_helper(kwargs, pay_period)

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

    start_date_obj = kwargs['start_date_obj']
    end_date_obj = kwargs['end_date_obj']

    pay_period = helpers.pay_period_helper(start_date_obj, end_date_obj)
    kwargs = helpers.kwargs_edit_helper(kwargs, pay_period)

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
