from app import parse_config_vars

def get_monthly_gross_income(annual_salary):
    gross_income = annual_salary / 12
    rounded_gross_income = round(gross_income)
    return rounded_gross_income

def get_tax_bracket(rounded_annual_salary):
    '''
    The only tax bracket that does not have a maximum amount is the largest,
    which was 180001+ , effective 2012. All brackets must have a minimum.
    '''
    all_tax_brackets = parse_config_vars.get_tax_brackets()

    for tax_bracket in all_tax_brackets:
        minimum = tax_bracket['range']['minimum']

        try:
            maximum = tax_bracket['range']['maximum']
        except KeyError:
            if minimum <= rounded_annual_salary:
                return tax_bracket

        if minimum <= rounded_annual_salary <= maximum:
            return tax_bracket

def get_monthly_income_tax(rounded_annual_salary, tax_bracket):
    '''
    $3,572 plus 32.5c for each $1 over $37,000
    (base_income_tax + extra_rate * (annual_salary - extra_threshold))
    '''

    base_income_tax = tax_bracket['base']
    extra_threshold = tax_bracket['extra']['threshold']
    extra_rate = tax_bracket['extra']['rate']

    extra_payable = rounded_annual_salary - extra_threshold
    extra_to_pay = extra_payable * extra_rate
    total_annual_income_tax = base_income_tax + extra_to_pay
    monthly_income_tax = total_annual_income_tax / 12

    rounded_monthly_income_tax = round(monthly_income_tax)

    return rounded_monthly_income_tax

def get_monthly_net_income(monthly_salary, monthly_income_tax):
    net_income = monthly_salary - monthly_income_tax
    return net_income

def get_superannuation(super_rate, gross_income):
    super_rate = super_rate / 100
    superannuation = super_rate * gross_income
    rounded_superannuation = round(superannuation)
    return rounded_superannuation
