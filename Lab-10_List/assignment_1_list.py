"""Q1. Write a Python program to sum all the items in a list."""

#Input(Enter the numbers separate by commas: 1,2,3 --> [1,2,3])
my_list = list(map(int,input("Enter the numbers separate by commas: ").split(",")))

#Logic
sum_num=0
for i in my_list:
    sum_num=sum_num+i

#Output
print(f"The sum of all the items in a {my_list} list is {sum_num}")
