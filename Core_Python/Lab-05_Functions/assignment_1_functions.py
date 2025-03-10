"""Q1. Declare a div() function with two parameters. Then call the function
and pass two numbers and display their division."""


#Declaring function : to perform division of two numbers
def div(dividend,divisor): 
    ''' This function returns the division of two numbers, where the divisor is not zero.
    If the divisor is zero, it returns an error message.'''
    if(divisor==0):
        return 'Can not divide by zero' # Error message if division by zero
    return round(dividend/divisor,3) # Return the result rounded to 3 decimal places

# Taking input from the user for the dividend and divisor
dividend=int(input("Enter the Dividend Number: "))
divisor=int(input("Enter the Divisor Number: "))

# Calling the div function to get the result
result=div(dividend,divisor)

# Display the result of the division
print(f"The Division of {dividend} and {divisor} is {result}")


        
"""
OUTPUT: Sample

Enter the Dividend Number: 10
Enter the Divisor Number: 3
The Division of 10 and 3 is 3.333
"""
