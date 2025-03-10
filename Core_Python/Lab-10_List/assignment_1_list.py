"""Q1. Write a Python program to sum all the items in a list."""

#Input(Enter the numbers separate by commas: 1,2,3 --> [1,2,3])
my_list = list(map(int,input("Enter the numbers separate by commas: ").split(",")))

# Initialize a variable to hold the sum of the numbers
total_sum=0

# Loop through each item in the list and add it to the total sum
for number in my_list:
    total_sum=total_sum+number

# Output the result
print(f"The sum of all the items in a {my_list} list is {total_sum}")


"""
OUTPUT:

Enter the numbers separate by commas: 1,2,3
The sum of all the items in a [1, 2, 3] list is 6
"""
