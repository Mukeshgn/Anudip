"""Q1. Write a Python program and calculate the mean of the below dictionary.

test_dict={"A": 6, "B": 9, "C": 5, "D" : 7, "E" :4}

Output: 6.2
"""
# Input dictionary
test_dict={"A": 6, "B": 9, "C": 5, "D" : 7, "E" :4}

# Initialize the sum of values to 0
total_sum=0

# Loop through all values in the dictionary and add them to the total_sum
for value in test_dict.values():
    total_sum=total_sum+value

# Calculate the mean by dividing the total sum by the number of items in the dictionary
mean=total_sum/len(test_dict)

# Output the result
print(mean)

"""
OUTPUT:

6.2
"""
