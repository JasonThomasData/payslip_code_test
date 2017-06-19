#!/usr/bin/env python3

'''
For initialising the database before the program is run.
'''

import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import parse_config_vars
from models import employee

def initialise_database(database_path):
    engine = create_engine(database_path, echo=True)
    employee.Employee.metadata.create_all(engine)
    return engine

def parse_csv(seed_data_path):
    parsed_seed_data = []
    with open(seed_data_path, 'r') as csv_file:
        seed_data = csv.DictReader(csv_file)
        for row in seed_data:
            parsed_seed_data.append(row)
    return parsed_seed_data

def seed_database(engine, seed_data):
    session = sessionmaker(bind=engine)()
    for row in seed_data:
        new_employee = employee.Employee(**row)
        session.add(new_employee)
    session.commit()

def main():
    database_path_configs = parse_config_vars.get_database_paths()
    database_path = database_path_configs['production']['sql_path']
    seed_data_path = database_path_configs['production']['seed_path']

    engine = initialise_database(database_path)
    seed_data = parse_csv(seed_data_path)
    seed_database(engine, seed_data)

if __name__ == "__main__":
    main()
