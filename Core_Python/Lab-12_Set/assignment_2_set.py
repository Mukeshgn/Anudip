"""Q2. Write a Python program to Return a set of elements present in Set A or B,but not both.

Input:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

Output:

{20, 70, 10, 60}
"""
# Input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Logic: Get the symmetric difference to find elements present in either set, but not both
set3=set1.symmetric_difference(set2)

# Output the result
print(set3)


"""
OUTPUT

{20, 70, 10, 60}
"""
