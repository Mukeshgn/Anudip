"""
Q1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.

Sample Output:
An array of 10 zeros:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
An array of 10 ones:
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
An array of 10 fives:
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
"""

# Importing the nimpy library for array operations
import numpy as np

# create an array of 10 zeros
zeros_array=np.zeros(10)
# Printing the array of 10 zeros
print("An array of 10 zeros:\n",zeros_array)

# Create an array of 10 ones
ones_array=np.ones(10)
# Printing the array of 10 ones
print("An array of 10 ones:\n",ones_array)

# Create an array of 10 fives
fives_array=np.ones(10)*5
print("An array of 10 fives:\n",fives_array)


"""
OUTPUT:Sample

An array of 10 zeros:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
An array of 10 ones:
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
An array of 10 fives:
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
"""
