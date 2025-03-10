"""
1Q. Suppose you have a dataset containing daily temperature readings for a city,
and you want to identify days with extreme temperature conditions. Find days
where the Temperature either exceeded 35 degrees Celsius hot day) or dropped below 5 degrees Celsius (cold day)

Input:

temperatures = np.array([32.5,34.2, 36.8,29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

Output:

Hot Days:
Days     Temperature(°C)
3 	 36.8
6 	 38.7
10 	 37.2

Cold Days:
Days     Temperature(°C)
11 	 4.0
14 	 -4.0
15 	 -12.0

"""

# importing numpy 
import numpy as np

# Given Input - temperature data 
temperatures = np.array([32.5,34.2, 36.8,29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4.0,5.6,6.5,-4.0,-12.0])

# Initialize dictionaries to store hot and cold days
hot_days={}
cold_days={}

# Iterate over the temperature data to classify hot and cold days
for day,temp in enumerate(temperatures,start=1):  # Using start=1 to treat day as 1-indexed
    if temp>35:
        hot_days[day]=temp # Adding to hot days dictionary
    elif temp<5:
        cold_days[day]=temp # Adding to cold days dictionary

# Output the results
print("Hot Days:")
print("Days     Temperature(°C)")# Alt+0176 for ° symbol
for day,temp in hot_days.items():
    print(day,"\t",temp)

print("\nCold Days:")
print("Days     Temperature(°C)")
for day,temp in cold_days.items():
    print(day,"\t",temp)


"""
OUTPUT:

Hot Days:
Days     Temperature(°C)
3 	 36.8
6 	 38.7
10 	 37.2

Cold Days:
Days     Temperature(°C)
11 	 4.0
14 	 -4.0
15 	 -12.0
"""
