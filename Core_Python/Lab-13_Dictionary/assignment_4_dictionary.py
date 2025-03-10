"""Q4. Write a Python program to get the key, value and item in a dictionary.

Input: input_dict={1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60)

Output:

Dictionary with Empty Items Dropped: {1:10, 2:20, 4: 40, 6: 60)
"""

# Input dictionary
input_dict={1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

# Logic to create a new dictionary with items that have non-None values
filtered_dict={key:value for key,value in input_dict.items() if value is not None}

# Output the filtered dictionary
print(f"Dictionary with Empty Items Dropped: {filtered_dict}")


"""
OUTPUT

Dictionary with Empty Items Dropped: {1: 10, 2: 20, 4: 40, 6: 60}
"""
