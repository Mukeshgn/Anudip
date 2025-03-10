"""Q3. Using max() and min() functions display the maximum and minimum of 5 random numbers. """

import random

# List to store 5 random numbers
random_numbers = []

# Generating 5 random numbers between 1 and 1000 and adding them to the list
for _ in range(5):
    random_numbers.append(random.randint(1,1000))

# Display the 5 random numbers
print(f"The 5 random numbers are : {random_numbers}")

# Finding and Displaying the maximum and minimum numbers using max() and min() functions
print(f"The maximum of 5 random numbers is : ",max(random_numbers))
print(f"The minimum of 5 random numbers is : ",min(random_numbers))



"""
OUTPUT: Sample

The 5 random numbers are : [161, 481, 868, 233, 774]
The maximum of 5 random numbers is :  868
The minimum of 5 random numbers is :  161
"""
