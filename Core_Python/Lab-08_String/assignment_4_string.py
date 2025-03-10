"""Q4. 4. Write a Python program to count and display the vowels of a given text 

String=”Welcome to python Training”
"""

# Given Input string
input_string="Welcome to python Training"
# Define the vowels
vowels="aeiou"
# Create a dictionary to store the count of each vowel
vowel_count={}

# Iterate through each character in the input string (converted to lowercase)
for char in input_string.lower():
    # If the character is a vowel, update its count in the dictionary
    if char in vowel_count:
        vowel_count[char]=vowel_count[char]+1
    elif char in vowels:
        vowel_count[char]=1

# Output the vowel count as a dictionary
print(vowel_count)

# Output the vowels and their counts without using a dictionary
print("The vowels of a given text are: ")
for vowel,count in vowel_count.items():
    print(vowel,"=",count)


"""
OUTPUT:

{'e': 2, 'o': 3, 'a': 1, 'i': 2}
The vowels of a given text are: 
e = 2
o = 3
a = 1
i = 2
"""

    
