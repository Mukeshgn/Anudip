"""Q4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.

Input:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

Output:

{40,50,30}
"""
# Input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Logic: Keep only the common elements between set1 and set2 using intersection
common_elements = set1.intersection(set2)

# Output the result
print(common_elements)


"""
OUTPUT

{40, 50, 30}
"""
