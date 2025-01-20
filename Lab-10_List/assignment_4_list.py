"""Q4. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

Original list: [1, 1, 2, 3, 4, 4, 5, 1] 

Length of the first part of the list: 3 

Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1]) """

#Input
my_list = [1, 1, 2, 3, 4, 4, 5, 1]
len_first_part = 3

#Logic
split_list=[]

first_part_list = my_list[:len_first_part]
second_part_list = my_list[len_first_part:]

split_list.append(first_part_list)
split_list.append(second_part_list)

#Output
print(f" plitted the said list into two parts: {tuple(split_list)}")
