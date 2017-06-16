### Assumptions

- The tax rates+thresholds will change often, so those should be stored in an easy-to-find config.yml file

- I can't be sure who the intended user for this program is going to be. I assume this is a prototype and if it works well then its features would be integrated into a larger monolith program; therefore the executable CLI should be thin. If this was intended for end users, a webapp/SaaS approach would be more appropriate but that's fine too because this program will be modular and easy to port to a web framework (using an MVC design pattern to make that painless).

- Assume that the monolith program/user might want to do processes in stages - update all employees' payslips, retrieve all employee's payslips. Not a feature we need to include this time.

- All employees are paid a salary, with no bonuses or overtime.

- The program is going to produce irregular results for different months, for example, March (31 days) and February (28/29 days). This app could be extended to take days of months into account. For now I'll assume the client knows this and provide what the client has asked, but the client should be asked to clarify this is what they want.

- Using text/csv might not scale well, depending on who the end user is. SQL scales well so use that. I'll have one table for employee's details. Use an ORM so we can have models to represent the tables in classes, and also since there's no indication which DB the client/employer uses, so PostgreSQL vs MySQL won't matter.

- Let's assume the company that needs this program might be large enough to have employees with the same name. Allow the user to retrieve employee data with employee id. Return an message if there are two of the same employees.

- Let's assume the client might want to use this program for generating EOY group certificates. This is another good reason to pursue an MVC pattern, so views can be added.

- Assume the client/employer would use Github and able to use TravisCI - that's what I'll use.

- Assume my client/employer in this project would use the Google Python Style guide.
