""" Q3. Write a Python program to find duplicate values from a list and display those."""

# Input: Taking comma-separated numbers from the user
my_list = list(map(int,input("Enter the number that separated by commas: ").split(",")))

# Logic: Finding duplicates
duplicate_num=[]
non_duplicate_num=[]
for number in my_list:
    if number not in non_duplicate_num: # Avoid adding the same duplicate multiple times
        non_duplicate_num.append(number)
    else:
        duplicate_num.append(number)

# Output: Displaying the list of duplicate values
print(f"The duplicate values from a {my_list} list is {duplicate_num}")


"""
OUTPUT
Enter the number that separated by commas: 1,2,3,1,2,5,6
The duplicate values from a [1, 2, 3, 1, 2, 5, 6] list is [1, 2]
"""
