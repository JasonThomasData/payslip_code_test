#!/usr/bin/env python3

'''
For initialising the database before the program is run.
'''

import parse_config_vars
import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import employee

def initialise_database():
    database_path = os.environ["DATABASE"]
    engine = create_engine(database_path, echo=True)
    employee.Employee.metadata.create_all(engine)
    return engine

def parse_csv():
    seed_data_path = os.environ["SEED_DATA"]
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

if __name__ == "__main__":
    engine = initialise_database()
    seed_data = parse_csv()
    seed_database(engine, seed_data)
