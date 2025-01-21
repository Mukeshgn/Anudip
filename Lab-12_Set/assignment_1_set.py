""" Q1. Write a Python program to Get Only unique items from two sets.

Input:

set1 = {10, 20, 30, 40, 50}

set2 = {30, 40, 50, 60, 70}

Output:

{70, 40, 10, 50, 20, 60, 30}"""

#Input
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#Logic
unique_items=set1.union(set2)

#Output
print(f"The unique items from {set1} and {set2} are {unique_items}")
