"""Q2. Write a Python program to remove a newline in Python 

String = "\nBest \nDeeptech \nPython \nTraining\n"
"""

#Given Input String
input_string="\nBest \nDeeptech \nPython \nTraining\n"

# Split the string by newline characters and store the result in a list
word_list=input_string.split("\n")

# Initialize an empty string to store the result
result_string=""

# Iterate through each word in the list and concatenate it to the result string
for word in word_list:
    result_string=result_string+word+" "
    
# Remove the trailing space and print the final result
print(result_string.strip())

"""
OUTPUT:
Best  Deeptech  Python  Training
"""
