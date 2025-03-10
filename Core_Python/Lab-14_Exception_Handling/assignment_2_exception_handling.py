"""
2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer
"""

try:
    # Declaring a integer Variable with name 'user_input'
    user_input=input("Enter the Integer Value: ")
    # Attempt to convert the input to an integer
    user_input=int(user_input)
except ValueError:
    # Raise a ValueError exception if the input cannot be converted to an integer
    print("Error: Invalid input! Please enter a valid integer.")
else:
    # Diplaying the valid integer input if no exception occurs
    print(f"You entered a valid integer: {user_input}")


"""
OUTPUT: Sample 1

Enter the Integer Value: 5
You entered a valid integer: 5


Sample 2

Enter the Integer Value: Anudip
Error: Invalid input! Please enter a valid integer.

"""
