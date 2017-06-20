### Using this program

I've simplified using this for the user, for a number of reasons. The user will only need to enter a user's first name, last name and start date to process and view a payslip. The employee's salary and superannuation rate are saved in the Employee table in the database. I have reasons, so please read my [assumptions](assumptions.md)

The program uses a CSV file to generate the required SQL table. The paths for the CSV and SQL databases are listed in a config.yml file in the root directory.

The tax rates the program uses are also stored in the config.yml file.

First thing, ensure the virtualenv is running:

    sourve venv/bin/activate

Generate the SQL tables:

	./seed.py

When that is finished, the SQL database will have a table of monthly wages for employees.

A second program will process one employee's payslip:

	./payslips.py --first_name John --last_name Smith --start_date 01-03-2017

If there are more than one employees with that name, the program will list the employees' unique IDs and ask you to pick one.

	./payslips.py --first_name John --last_name Smith --start_date 01-03-2017 --id 4

When finished, deactivate the virtualenv:

    deactivate
