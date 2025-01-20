""" Q3. Write a Python program to find duplicate values from a list and display those."""

#input
my_list = list(map(int,input("Enter the number that separated by commas: ").split(",")))

#Logic
duplicate_num=[]
non_duplicate_num=[]
for num in my_list:
    if num not in non_duplicate_num:
        non_duplicate_num.append(num)
    else:
        duplicate_num.append(num)

#Output
print(f"The duplicate values from a {my_list} list is {duplicate_num}")

