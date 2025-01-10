"""Q1. Declare a div() function with two parameters. Then call the function
and pass two numbers and display their division."""

#Declaring function
def div(num_1,num_2): 
    ''' This function returns division of two numbers,where num2 is not zero'''
    if(num_2==0):
        return 'Can not divide by zero'
    return round(num_1/num_2,3)

#Input
num_1=int(input("Enter the Dividend Number: "))
num_2=int(input("Enter the Divisor Number: "))

#calling function
result=div(num_1,num_2)

#Output
print(f"The Division of {num_1} and {num_2} is {result}")

        
