"""
2. Suppose you have a dataset containing monthly sales data for a company,
and you want to split this data into quarterly reports for analysis and reporting purposes.

Input:
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

Output:

Quarter 1 Sales (in thousands of dollars): 
[120 135 148]

Quarter 2 Sales (in thousands of dollars): 
[165 180 155]

Quarter 3 Sales (in thousands of dollars): 
[168 190 205]

Quarter 4 Sales (in thousands of dollars): 
[198 210 225]
"""
# Importing Numpy
import numpy as np

# Given monthly sales data
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Split the array into 4 equal parts (quarters)
quarters = np.split(monthly_sales,4)

# Output the split parts
for i,quarter in enumerate(quarters, start=1):
    print(f"Quarter {i} Sales (in thousands of dollars): \n{quarter}\n")

"""
OUTPUT

Quarter 1 Sales (in thousands of dollars): 
[120 135 148]

Quarter 2 Sales (in thousands of dollars): 
[165 180 155]

Quarter 3 Sales (in thousands of dollars): 
[168 190 205]

Quarter 4 Sales (in thousands of dollars): 
[198 210 225]
"""
