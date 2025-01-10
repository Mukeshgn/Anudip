"""Q2. Declare a square() function with one parameter. Then call the function and
pass one number and display the square of that number ."""

#Declaring function
def square(num):
    '''This function return the square root of num'''
    return num**2

#Input
num=int(input("Enter the Number: "))

#Calling function
result=square(num)

#Output
print(f"The Square of {num} is {result}")
