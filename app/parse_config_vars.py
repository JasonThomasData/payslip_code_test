import os
import yaml

'''
Must be loaded at the start of any process to parse the config.yml
'''

with open('config.yml', 'r') as config_file:
    config_data = yaml.load(config_file)
    database_path = config_data["data"]["database"]
    os.environ["DATABASE"] = database_path
