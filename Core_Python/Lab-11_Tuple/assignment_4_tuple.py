"""Q4.Write a python program and iterate the given tuples 

Input: 

employee1 = ("John Doe", 101, "Human Resources", 60000) 
employee2 = ("Alice Smith", 102, "Marketing", 55000) 
employee3 = ("Bob Johnson", 103, "Engineering", 75000)"""

# Input: Employee data in the form of tuples
employee1 = ("John Doe", 101, "Human Resources", 60000) 
employee2 = ("Alice Smith", 102, "Marketing", 55000) 
employee3 = ("Bob Johnson", 103, "Engineering",75000)

# Logic: Combine all employee tuples into a list and iterate over them
employees=(employee1,employee2, employee3)

# Iterate through each employee tuple and display their details
for employee in employees:
    print(f"Name: {employee[0]}, ID: {employee[1]}, Department: {employee[2]}, Salary: {employee[3]}")


"""
OUTPUT

Name: John Doe, ID: 101, Department: Human Resources, Salary: 60000
Name: Alice Smith, ID: 102, Department: Marketing, Salary: 55000
Name: Bob Johnson, ID: 103, Department: Engineering, Salary: 75000
"""
