### Assumptions

- The tax rates+thresholds will change often, so those should be stored in an easy-to-find config/yml file

- I can't be sure who the intended user for this program is going to be. I assume this is a prototype and if it works well then its features would be integrated into a larger monolith program; therefore the executable CLI should be thin. If this was intended for end users, a webapp/SaaS approach would be more appropriate but that's fine too because this program will be modular and easy to port to a web framework (using an MVC design pattern to make that painless).

- Assume that the monolith program/user might want to do processes in stages - update all employees' payslips, retrieve all employee's payslips. In future the user might like to update/see a single employee's payslip. 

- Using text/csv might not scale well, depending on who the end user is. SQL scales well so use that. I'll have one table for employee's pay details and one table for their payslips. Use an ORM so we can have models to represent the tables in classes.

- Let's assume each employee's payment records would be created monthly, perhaps by a payroll service/staff member. Each employee should have as many records as there are months of employment. The user/monolith program will want to process payslips for one particular month, but in future they may also wish to retrieve data from several months (for an EOY group certificate, etc).

- Assume the client/employer would use Github and able to use TravisCI - that's what I'll use.

- Assume my client/employer in this project would use the Google Python Style guide.
