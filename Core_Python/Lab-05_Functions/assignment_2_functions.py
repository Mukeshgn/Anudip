"""Q2. Declare a square() function with one parameter. Then call the function and
pass one number and display the square of that number ."""


#Declaring function to calculate the square of a number
def square(number):
    '''This function returns the square of the given number. It multiplies the number by itself to calculate the square.'''
    return number**2

# Taking input from the user
number=int(input("Enter the Number: "))

# Calling the square function to get the result
result=square(number)

# Displaying the result
print(f"The Square of {number} is {result}")



"""
OUTPUT:Sample

Enter the Number: 5
The Square of 5 is 25
"""
