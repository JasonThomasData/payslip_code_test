import yaml

'''
Must be loaded at the start of any process to parse the config.yml
'''

def read_config_file():
    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file)
        return config_data

def get_database_paths():
    config_data = read_config_file()
    database_paths = config_data["data_paths"]
    return database_paths

def get_cli_allowed_args():
    config_data = read_config_file()
    required_args = config_data["payslips_cli"]["arguments"]["required"]
    optional_args = config_data["payslips_cli"]["arguments"]["optional"]
    return required_args, optional_args

def get_tax_brackets():
    config_data = read_config_file()
    tax_brackets = config_data['tax_brackets']
    return tax_rates

def get_required_date_formats():
    config_data = read_config_file()
    date_formats = config_data['dates']
    return date_formats
