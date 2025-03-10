"""3. Write a Python program to count Uppercase, Lowercase, special character
and numeric values in a given string Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

Output: 

UpperCase : 5 

LowerCase : 18 

NumberCase : 5 

SpecialCase : 11 """

"""3. Write a Python program to count Uppercase, Lowercase, special character
and numeric values in a given string Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

Output: 

UpperCase : 5 

LowerCase : 18 

NumberCase : 5 

SpecialCase : 11 """

# Input string
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Initializing counters for uppercase, lowercase, numbers, and special characters
uppercase=0
lowercase=0
numbers=0
special=0

# Loop through each character in the input string
for i in input_string:
    if(i.isupper()):  # Check if character is uppercase
        uppercase=uppercase+1
    elif(i.islower()): # Check if character is lowercase
        lowercase=lowercase+1
    elif(i.isdigit()): # Check if character is a digit
        numbers=numbers+1
    else: # If it's neither a letter nor a digit, it's considered a special character
        special=special+1

# Print the results
print(f"UpperCase = {uppercase} \nLowerCase = {lowercase} \nNumbers = {numbers} \nSpecial = {special}")


"""
OUTPUT:
UpperCase = 5 
LowerCase = 18 
Numbers = 5 
Special = 11
"""
