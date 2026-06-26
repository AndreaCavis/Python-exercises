'''
Alright, Space Explorer, let's put that newfound knowledge of yours to use! Picture this: 
there's a company out there looking to reward their high-performing developers with a well-deserved 15% bump in salary. 
Your mission is to march into their employee database and make it happen. The database is just a list of dictionaries, 
with each dictionary serving as the ID card for an employee. A couple of keys to notice here are 'role' and 'salary': 
    'role' holds the job title, and 
    'salary' is the yearly paycheck. 
Your job? Simple: hunt down those developers and give their salary a 15% jet boost.

Now, here's some technical jargon for you: the task involves iterating over a list of dictionaries. Each dictionary represents an employee, 
including their role and salary, among other attributes. You are to apply a 15% salary increment for employees with the role of 'developer'.

Remember, it's important to preserve the integrity of the database and not to affect any data unrelated to the developer's salary. Best of luck, Voyager!
'''


def salary_increment(employees: list[dict]) -> list[dict]:
    bonus = 0.15
    for employee in employees:
        if employee['role'] == 'developer':
            employee['salary'] += employee['salary'] * bonus
    return employees

# Test cases

employees = [{
    'name': 'John',
    'role': 'developer',
    'salary': 50000
}, {
    'name': 'Mary',
    'role': 'developer',
    'salary': 70000
}, {
    'name': 'Jim',
    'role': 'manager',
    'salary': 85000
}]

print(salary_increment(employees))