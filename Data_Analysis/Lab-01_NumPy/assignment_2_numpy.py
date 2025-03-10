"""
2. Convert the below list into a numpy array then display the array then display 
the first and last index and then multiply each element by 2 and display the result.
Input: my_list = [1, 2, 3, 4, 5]
Output:
First element: 1
Last element: 5
Array after doubling each element: [2 4 6 8 10]
"""
# import the numpy library
import numpy as np
# Given Input: Define the List
my_list=[1,2,3,4,5]
# Convert the list to a NumPy array
numpy_array=np.array(my_list)
#  Get first and last element
first_element=numpy_array[0]
last_element=numpy_array[-1]
#Multuply each element
doubled_array=numpy_array*2
# Displaying the first element, last element and multiply each element by 2
print("First element:",first_element)
print("Last element:",last_element)
print("Array after doubling each element:",doubled_array)
