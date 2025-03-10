"""Q3. Write a Python program to get the key, value and item in a dictionary.

input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Output:

key value
1   10
2   20
3   30
4   40
5   50
6   60
"""
# Input dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Logic to display the key-value pairs
print("Key  Value")  # Header for better formatting
for key,val in dict_num.items():
    print(f"{key}    {val}") # Display each key-value pair

"""
OUTPUT:

Key  Value
1    10
2    20
3    30
4    40
5    50
6    60
"""
