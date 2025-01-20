"""Q3.Write a Python program to calculate the sum of the numbers in a given tuple.

 Input:

 tuples_list = [(1, 2), (3, 4), (5, 6)]
"""

#Input
tuples_list = [(1, 2), (3, 4), (5, 6)]

#Logic
tuple_sum=0
for tuple_1 in tuples_list:
    tuple_sum=tuple_sum+sum(tuple_1)

#Output
print(f"The sum of the numbers in a given tuple{tuples_list} is {tuple_sum}")
