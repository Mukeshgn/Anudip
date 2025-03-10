#Q3. Write a Program to Convert Kilometers to Miles

#Input: Declaring an float variables named 'kilometers_distance'
kilometers_distance=float(input("Enter the distance in Kilometers: "))

# Logic: Convert kilometers to miles using the conversion factor
kilometers_to_miles_factor=0.621371
miles_distance=kilometers_distance*kilometers_to_miles_factor

# Display the distance in miles
print(f"{kilometers_distance} kilometers is equal to {miles_distance} Miles.")



"""
OUTPUT: Sample

Enter the distance in Kilometers: 10
10.0 kilometers is equal to 6.21371 Miles.
"""
