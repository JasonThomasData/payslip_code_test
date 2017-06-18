import os
import yaml

'''
Must be loaded at the start of any process to parse the config.yml
'''

def get_database_paths():
    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file)
        database_paths = config_data["data_paths"]
        return database_paths

def get_cli_allowed_args():
    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file)
        required_args = config_data["payslips_cli"]["arguments"]["required"]
        optional_args = config_data["payslips_cli"]["arguments"]["optional"]
        return required_args, optional_args

