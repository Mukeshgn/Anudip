"""Q3. Write a Python program to Check if two sets have any elements in common.
If yes, display the common elements.

Input:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

Output:

{10}
"""

# Input sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Logic: Find the intersection of the two sets to get common elements
common_elements=set1.intersection(set2)

# Output the result
if(len(common_elements)>0):
    print(common_elements)
else:
    print(f"There is no common elements from {set1} and {set2}")


"""
OUTPUT

{10}
"""
