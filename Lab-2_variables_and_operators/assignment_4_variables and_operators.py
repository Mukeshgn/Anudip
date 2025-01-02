#Q4. Python program to find the area of a triangle whose sides are given

import math

#Input
side_1=float(input("Enter the base side of the triangle: "))
side_2=float(input("Enter the height side of the triangle: "))
side_3=float(input("Enter the height side of the triangle: "))

#Logic(area of a triangle)
side=(side_1+side_2+side_3)/2
area=math.sqrt(side * (side - side_1) * (side - side_2) * (side - side_3))

#Output
print(f"The area of a triangle whose sides are {side_1},{side_2} and {side_3} is {area}")
