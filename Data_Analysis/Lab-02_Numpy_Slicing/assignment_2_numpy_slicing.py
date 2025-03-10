"""
Q2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

Sample Output:
[[2 3 4]
 [5 6 7]
 [8 9 10]]

"""
# Importing the NumPy library
import numpy as np

# Create a 1D array with values ranging from 2 to 10
values=np.arange(2,11)

# Reashape the 1D array  into a 3x3 matrix
matrix=values.reshape(3,3)

# Display the resulting matrix
print(matrix)

"""
OUTPUT:Sample

[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]

"""
