"""Q3. Write a Python program to Check if two sets have any elements in common.
If yes, display the common elements.

Input:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

Output:

{10}
"""

#Input

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

#Logic(intersection)
result=set1.intersection(set2)

#Output
if(len(result)>0):
    print(f"The common elements from {set1} and {set2} are {result}")
else:
    print(f"There is no common elements from {set1} and {set2}")
