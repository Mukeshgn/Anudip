"""Q3. Write a Python program to reverse words in a string 

String = “Deeptech Python Training”
"""

# Given Input String
input_str="Deeptech Python Training"

# Split the string into a list of words using space
word_list=input_str.split(" ")

# Initialize an empty string to store the result
reversed_string=""

# Iterate through each word in the word list
for word in word_list:
    # Reverse each word using slicing [::-1] and concatenate it to the result string
    reversed_string=reversed_string+word[::-1]+" "
    
# Remove the trailing space and print the final reversed string
print(reversed_string.strip())

"""
OUTPUT:
hcetpeeD nohtyP gniniarT
"""
