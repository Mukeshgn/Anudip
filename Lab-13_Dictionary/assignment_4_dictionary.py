"""Q4. Write a Python program to get the key, value and item in a dictionary.

Input: input_dict={1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60)

Output:

Dictionary with Empty Items Dropped: {1:10, 2:20, 4: 40, 6: 60)
"""
#Input
input_dict={1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

#Logic
result={key:value for key,value in input_dict.items() if value is not None}

#Output
print(f"Dictionary with Empty Items Dropped: {result}")
