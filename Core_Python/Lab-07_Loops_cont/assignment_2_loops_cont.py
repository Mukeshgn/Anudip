#Q2. Python program to check if the given string is a palindrome

#Input: Take a string from user
input_string=input("Enter the String: ")

#Revers the String
reversed_string=""
for char in input_string:
    reversed_string=char+reversed_string # Add each character to the front

# Check if the string is a palindrome
if(input_string==reversed_string):
    # If the original string is the same as the reversed one
    print(f"{input_string} is a Palindrome")
else:
    # If the original string is not the same as the reversed one
    print(f"{input_string} is not a Palindrome")


"""
OUTPUT: Sample 1

Enter the String: madam
madam is a Palindrome

Sample 2

Enter the String: Anudip
Anudip is not a Palindrome
"""
