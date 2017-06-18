#!/usr/bin/env python3

'''
The CLI has the responsibility for terminal interaction only, like a thin
client.
'''

import parse_config_vars
import sys
#from controllers import make_payslip

def check_required_arguments(required_args, parsed_args):
    '''
    This is to alert the user in case a required CLI arg was not entered
    '''
    try:
        for arg in required_args:
            parsed_args[arg]
    except KeyError:
        err_message = "The program requires --{} <VALUE>".format(arg)
        raise Exception(err_message)

def parse_arguments(allowed_args, provided_args):
    required_args = ['first_name', 'last_name', 'start_date', 'end_date']
    optional_args = ['id']
    allowed_args = required_args + optional_args

    parsed_args = {}

    while(len(provided_args) > 1):
        first_arg = provided_args.pop(0)

        key = first_arg.replace("--", "")
        if key in allowed_args:
            value = provided_args.pop(0)
            parsed_args[key] = value

    return parsed_args

if __name__ == "__main__":
    '''
    The 'result' will be an error message or the message formed in a view.
    '''

    required_args = ['first_name', 'last_name', 'start_date', 'end_date']
    optional_args = ['id']
    allowed_args = required_args + optional_args

    porivded_args = sys.argv
    parsed_args = parse_arguments(allowed_args, provided_args)
    check_required_arguments(required_args, parsed_args)
    result = make_payslip.one_employee(parsed_args)

    print(result)