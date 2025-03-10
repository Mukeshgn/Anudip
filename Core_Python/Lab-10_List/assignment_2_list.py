"""Q2. Write a Python program to get the largest and smallest number from a list without builtin functions."""

# Input: Enter numbers separated by commas
my_list=list(map(int,input("Enter the number that separated by commas: ").split(",")))

# Initialize the smallest and largest number to the first number in the list
smallest_number=my_list[0]
largest_number=my_list[0]

# Loop through the list to find the smallest and largest numbers
for number in my_list:
    if number < smallest_number:
        smallest_number = number
    elif number > largest_number:
        largest_number = number

# Output the results
print(f"The largest number from a {my_list} list is {largest_number}\nThe smallest number from a {my_list} list is {smallest_number}")

"""
OUTPUT:
Enter the number that separated by commas: 3,5,7,8
The largest number from a [3, 5, 7, 8] list is 8
The smallest number from a [3, 5, 7, 8] list is 3
"""
