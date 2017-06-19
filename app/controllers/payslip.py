from app.models import employee
from app.views import payslip_view
from app.controllers.concerns import date_parse, payg_calc

def one_employee(**args):
    '''
    For a single employee, process their data and generate one payslip.
    '''
    start_date = args['start_date']
    start_date_obj, end_date_obj = date_parse.get_pay_period(start_date)

    try:
        employee_id = args['id']
        employee_record = employee.Employee.get_by_id(employee_id)
    except KeyError:
        first_name = args['first_name']
        last_name = args['last_name']
        employee_record = employee.Employee.get_by_name(first_name, last_name)

    annual_salary = employee_record.annual_salary
    super_rate = employee_record.superannuation_rate

    tax_bracket = payg_calc.get_tax_bracket(annual_salary)

    gross_income = payg_calc.get_monthly_gross_income(annual_salary)
    income_tax = payg_calc.get_monthly_income_tax(annual_salary, tax_bracket)
    net_income = payg_calc.get_monthly_net_income(gross_income, income_tax)
    superannuation = payg_calc.get_superannuation(super_rate, gross_income)

    payslip = payslip_view.as_blob(first_name=args['first_name'],
                                   last_name=args['last_name'],
                                   start_date_obj=start_date_obj,
                                   end_date_obj=end_date_obj,
                                   net_income=net_income,
                                   income_tax=income_tax,
                                   gross_income=gross_income,
                                   superannuation=superannuation)
    return payslip
