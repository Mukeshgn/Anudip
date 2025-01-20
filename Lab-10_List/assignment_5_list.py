"""Q5. Write a Python program to traverse a given list in reverse order,and print the
elements with the original index. Original list: ['red', 'green', 'white', 'black'] 

Traverse the said list in reverse order: 

black 

white 

green

red

"""
#Input
my_list = ['red', 'green', 'white', 'black']

for i in range(len(my_list)-1,-1,-1):
    print(my_list[i],"--> Original Index:", i)
