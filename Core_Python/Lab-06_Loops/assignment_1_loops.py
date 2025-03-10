#Q1. Write a python program to reverse a number using a while loop.

# Input: Declaring an integer variables named 'number' 
number=int(input("Enter the number: "))

# Storing the original number for displaying the output later
original_number=number

# Logic to reverse the number using a while loop
reversed_number=0 # Variable to store the reversed number
while(number>0):
    digit=number%10 # Extract the last digit
    reversed_number=reversed_number*10+digit # Build the reversed number
    number=number//10 # Remove the last digit from the number


# Display the reversed number
print(f"The Reverse number of {original_number} is {reversed_number}")


"""
OUTPUT: Sample

Enter the number: 12345
The Reverse number of 12345 is 54321
"""
