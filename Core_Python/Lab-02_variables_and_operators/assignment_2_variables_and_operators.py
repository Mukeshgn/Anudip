#Q2. Declare two variables and print that which variable is largest using ternary operators 

# Declaring an integer variable named 'first_variable' and 'second_variable'
first_variable=int(input("Enter the Number for first variable: "))
second_variable=int(input("Enter the Number for second variable: "))

# Logic: Determine the largest variable using a ternary operator
largest_variable=first_variable if first_variable> second_variable else second_variable

# Display which variable is the largest
print(f"{largest_variable} is the largest variable among {first_variable} and {second_variable}")



"""
OUTPUT: Sample

Enter the Number for first variable: 10
Enter the Number for second variable: 5
10 is the largest variable among 10 and 5
"""
