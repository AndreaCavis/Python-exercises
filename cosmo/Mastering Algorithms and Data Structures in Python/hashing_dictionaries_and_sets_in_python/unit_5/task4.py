'''
Well done, Space Voyager! We're on the home stretch; this is the last practice exercise for hash tables. 
You've aced all the tasks thus far, but can you handle this one on your own?

In our HR system, we maintain an employee database. Each employee is assigned a unique ID, 
and their role is tracked against this ID in a Python dictionary, which constitutes our hash table. 
Your task is to create an initial database with various roles, then simulate a scenario involving a promotion 
and an employee departure while updating the database accordingly.

Remember, this requires the addition, retrieval, and deletion operations that we've learned about 
in addition to the time complexity analysis for these operations. Good luck!
'''

# TODO: Create a Python dictionary to serve as a hash table
employees = dict()

# TODO: Add employee names with their roles to the dictionary
employees["Mark"] = "Junior Software Developer"
employees["Tony"] = "Senior Software Developer"
employees["Clara"] = "Front-End Developer"
employees["Claude"] = "Team Manager"

# TODO: Print the initial employee database
for name, role in employees.items():
    print(f"Employee: {name}, Role: {role}")

# TODO: Update the role of an employee in the database
employees["Mark"] = "Software Developer"

# TODO: Print the database after the employee role update
print("\nUpdated employees")
for name, role in employees.items():
    print(f"Employee: {name}, role: {role}")

# TODO: Remove an employee from the database
del employees["Tony"]

# TODO: Print the final employee database after the removal
print("\nUpdated employees")
for name, role in employees.items():
    print(f"Employee: {name}, role: {role}")