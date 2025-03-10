"""
Q4. Write a NumPy program to convert a list and tuple into arrays.

Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8]

Input: my_tuple = ([8, 4, 6], [1, 2, 3])

Sample Output:
List to array:
[1 2 3 4 5 6 7 8]
Tuple to array:
[[8 4 6]
 [1 2 3]]
"""

# Importing the Numpy library
import numpy as np

# Given Inputs
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

# Convert list into a Numpy array
array_from_list=np.array(my_list)

# Convert tuple into a Numpy array
array_from_tuple=np.array(my_tuple)

# Display the results
print(f"List to array:\n{array_from_list}")
print(f"Tuple to array:\n{array_from_tuple}")


"""
Output: Sample

List to array:
[1 2 3 4 5 6 7 8]
Tuple to array:
[[8 4 6]
 [1 2 3]]
"""
