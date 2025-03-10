"""
1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
"""

# Declaring integer Variable with name 'dividend' and 'divisor'
dividend=int(input("Enter the Dividend Number: "))
divisor=int(input("Enter the Divisor Number: "))

try:
    #Attempt to divide a numbers
    result=dividend/divisor
except ZeroDivisionError:
    # Handle the case when divisor is zeo
    print("Error: Division by zeo is not allowed.")
else:
    # Display the result if no divisor is Zero
    print(f"Division of {dividend} and {divisor} is {result}")


"""
OUTPUT: Sample 1

Enter the Dividend Number: 5
Enter the Divisor Number: 0
Error: Division by zeo is not allowed.

Sample 2

Enter the Dividend Number: 5
Enter the Divisor Number: 2
Division of 5 and 2 is 2.5
"""
