"""Q2. Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary:

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

Expected Result: (1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
# Input dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

# Logic to concatenate dictionaries using the 'update' method
concatenated_dict=dic1.copy() # Create a copy of dict1 to avoid modifying the original
concatenated_dict.update(dic2) # Add dict2 to the copied dict
concatenated_dict.update(dic3)  # Add dict3 to the concatenated dict

# Output the result
print(concatenated_dict)


"""
OUTPUT:

{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
