"""Q2. Write a Python program to get the largest and smallest number from a list without builtin functions."""

#Input
my_list=list(map(int,input("Enter the number that separated by commas: ").split(",")))

#Logic
min_num=my_list[0]
max_num=my_list[0]

for num in my_list:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num

#Output
print(f"The largest number from a {my_list} list is {max_num}\nThe smallest number from a {my_list} list is {min_num}")
