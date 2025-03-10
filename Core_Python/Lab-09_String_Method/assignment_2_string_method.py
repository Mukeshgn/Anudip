"""2. Write a Python program to remove duplicate characters of a given string. 

Input = “String and String Function” 

Output: String and Function """

# Given Input String
input_string="String and String Function"

# Initialize an empty string to store the result without duplicate words
unique_words=""

# Split the input string into individual words and loop through them
for word in input_string.split():
    # Check if the word is not already in the result string
    if word not in unique_words:
        unique_words=unique_words+word+" " # Add the word to the result string

# Strip any trailing spaces from the result string
result=unique_words.strip()
# Print the result
print(result)

"""
OUTPUT

String and Function
"""
