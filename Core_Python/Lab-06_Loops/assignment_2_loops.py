#Q2. Write a python program to check whether a number is palindrome or not

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

# Logic to check if the number is a palindrome
if(original_number==reversed_number):
    print(f"The Given {original_number} is palindrome")
else:
    print(f"The Given {original_number} is not a palindrome")


"""
OUTPUT: Sample 1

Enter the number: 121
The Given 121 is palindrome

OUTPUT: Sample 2

Enter the number: 123
The Given 123 is not a palindrome
"""
