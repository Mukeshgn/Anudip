#Q3. Write a python program finding the factorial of a given number using a while loop. 


# Input: Declaring an integer variables named 'number' 
number=int(input("Enter the positive number: "))

# Storing the original number for display purposes
original_number = number

# Logic to calculate the factorial using a while loop
factorial=1 # Initialize the factorial variable
if(number==0):
     # Factorial of 0 is 1
    print(f"The factorial of {original_number}! = 1")
else:
    while(number>0):
        factorial=factorial*number  # Multiply factorial by the current number
        number=number-1 # Decrement the number
    print(f"The factorial of {original_number}! = {factorial}")


"""
OUTPUT: Sample

Enter the positive number: 5
The factorial of 5! = 120
"""
