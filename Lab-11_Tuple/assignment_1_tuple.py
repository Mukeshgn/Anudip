""" Q1. Write a Python program to find the number of times 4 appears in the tuple. 

Input: 

tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
"""
#Input
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
#Logic(using count() function)
count=tuplex.count(4)
#Output
print(f"The number of times 4 appears in the tuple is {count}")
