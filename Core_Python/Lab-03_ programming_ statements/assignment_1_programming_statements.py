#Q1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

# Declaring an int variables named 'number'
number=int(input("Enter the Number: "))

# Logic: Using a ternary operator to check whether the number is even or odd
number_type = "Even" if number%2==0 else "Odd"

# Display whether the number is even or odd
print(f"The Given number {number} is {number_type}.")



"""
OUTPUT: Sample

Enter the Number: 5
The Given number 5 is Odd.
"""
