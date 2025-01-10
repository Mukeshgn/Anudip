"""Q3. Using max() and min() functions display the maximum and minimum of 5 random numbers. """

import random

random_numbers = []

for _ in range(5):
    random_numbers.append(random.randint(1,1000))

print(f"The 5 random numbers are : {random_numbers}")
print(f"The maximum of 5 random numbers is : ",max(random_numbers))
print(f"The minimum of 5 random numbers is : ",min(random_numbers))
