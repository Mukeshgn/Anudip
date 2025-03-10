"""Q3.Write a Python program to calculate the sum of the numbers in a given tuple.

 Input:

 tuples_list = [(1, 2), (3, 4), (5, 6)]
"""

# Input: A list of tuples, each containing two numbers
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Logic: Initialize a variable to store the sum of the numbers
total_sum=0

# Iterate through each tuple in the list and calculate the sum of its elements
for single_tuple in tuples_list:
    total_sum=total_sum+sum(single_tuple)

# Output: Display the sum of all numbers in the given tuples
print(f"The sum of the numbers in a given tuple{tuples_list} is {total_sum}")

"""
OUTPUT
The sum of the numbers in a given tuple[(1, 2), (3, 4), (5, 6)] is 21
"""
