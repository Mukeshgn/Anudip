"""Q5. Write a Python program to traverse a given list in reverse order,and print the
elements with the original index. Original list: ['red', 'green', 'white', 'black'] 

Traverse the said list in reverse order: 

black 
white 
green
red

"""
# Input: Original list of colors
my_list = ['red', 'green', 'white', 'black']

# Logic: Traverse the list in reverse order and print each element with its original index
for index in range(len(my_list)-1,-1,-1):
    print(my_list[index],"--> Original Index:", index)


"""
OUTPUT

black --> Original Index: 3
white --> Original Index: 2
green --> Original Index: 1
red --> Original Index: 0
"""

