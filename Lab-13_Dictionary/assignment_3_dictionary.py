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
#Input
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#Logic
print("Key  Value")
for key,val in dict_num.items():
    print(f"{key}    {val}")
