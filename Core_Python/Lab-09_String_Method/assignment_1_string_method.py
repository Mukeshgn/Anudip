"""1. Write a Python program to Count all letters, digits, and special symbols from the given string 

Input = “P@#yn26at^&i5ve” 

Output: Chars = 8 Digits = 2 Symbol = 3 """

# Given Input string
input_string = "P@#yn26at^&i5ve"

# Initializing counters for letters, digits, and symbols
num_letters=0
num_digits=0
num_symbols=0

# Loop through each character in the input string
for char in input_string:
    if(char.isalpha()): # Check if character is an alphabet
        num_letters=num_letters+1
    elif(char.isdigit()): # Check if character is a digit
        num_digits=num_digits+1
    else: # If it's neither a letter nor a digit, it's considered a symbol
        num_symbols=num_symbols+1

# Print the results
print(f"Chars = {num_letters} Digits = {num_digits} Symbols={num_symbols}")


"""
OUTPUT:
Chars = 8 Digits = 3 Symbols=4
"""
        
