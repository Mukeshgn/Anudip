#Q4. Python program to find the area of a triangle whose sides are given

import math

# Declaring an float variables named 'first_side' ,'second_side' and 'third_side'
first_side=float(input("Enter the length of the first side of the triangle: "))
second_side=float(input("Enter the length of the second side of the triangle: "))
third_side=float(input("Enter the length of the third side of the triangle: "))

#Logic
# Calculate the semi-perimeter of the triangle
semi_perimeter=(first_side+second_side+third_side)/2

# Calculate the area using Heron's formula
area=math.sqrt(semi_perimeter * (semi_perimeter - first_side) * (semi_perimeter - second_side) * (semi_perimeter - third_side))

# Display the area of the triangle
print(f"The area of a triangle whose sides are {first_side},{second_side} and {third_side} is {area:.2f}")



"""
OUTPUT: Sample

Enter the length of the first side of the triangle: 5
Enter the length of the second side of the triangle: 6
Enter the length of the third side of the triangle: 7
The area of a triangle whose sides are 5.0,6.0 and 7.0 is 14.70
"""
