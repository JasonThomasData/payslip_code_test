import math
from app.models import employee
from app.views import payslip_view
from app import parse_config_vars

def get_pay_period(start_date, end_date):
    '''
    Get the end day of this month.
    '''
    pass

def get_monthly_salary(annual_salary):
    monthly_salary = annual_salary / 12
    rounded_monthly_salary = math.floor(monthly_salary)
    return monthly_salary

def get_monthly_income_tax(annual_salary):
    tax_rates = parse_config_vars.get_tax_rates()
    print(tax_rates)
    return 1

def get_net_income():
    return 1

def get_superannuation():
    return 1

def one_employee(first_name, last_name, start_date, end_date):
    '''
    For a single employee, process their data and generate one payslip.
    '''

    '''
    try:
        parsed_start_date
        parsed_end_date
    except SomeDateError:
        err_message = "Your dates are not valid, please check them."
        return err_message
    '''

    all_employee_records = employee.Employee.get_by_name(first_name, last_name)

    if len(all_employee_records) == 0:
        err_message = """There is no database record of an employee called
        {} {}.""".format(first_name, last_name)
        return err_message
    elif len(all_employee_records) != 1:
        err_message = """There is more than one employee called {} {}. Try
        retrieving the record with --employee_id NUMBER. Valid employee_id
        numbers are {}""".format(first_name, last_name, 1)
        return err_message
    else:
        employee_record = all_employee_records[0]

    gross_income = get_monthly_salary(employee_record.annual_salary)
    income_tax = get_monthly_income_tax(employee_record.annual_salary)
    net_income = get_net_income()
    superannuation = get_superannuation()
    name = first_name + last_name

    payslip = payslip_view.as_blob(first_name=first_name,
                                   last_name=last_name,
                                   start_date=start_date,
                                   end_date=end_date,
                                   net_income=net_income,
                                   income_tax=income_tax,
                                   gross_income=gross_income,
                                   superannuation=superannuation)
    return payslip
