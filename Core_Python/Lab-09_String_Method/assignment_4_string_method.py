""" 4. Write a Python Count vowels in a string 

input= “Welcome to Python Assignment” 

Output: Total vowels are: 8 """

# Given Input String
input_string = "Welcome to Python Assignment"

# Initializing counter for vowels
vowel_count=0

# Defining the set of vowels (both uppercase and lowercase)
vowels="aeiouAEIOU"

# Loop through each character in the input string
for char in input_string:
    if char in vowels: # Check if character is a vowel
        vowel_count=vowel_count+1  # Increment the vowel count

# Print the result
print(f"Total vowels are: {vowel_count}")


"""
OUTPUT:
Total vowels are: 8
"""
