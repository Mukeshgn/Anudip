"""Q2. Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary:

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Expected Result: (1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
#Input
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

#Logic(Using Update)
result=dic1.copy()
result.update(dic2)
result.update(dic3)

#Output
print(f"The concatenation of {dic1},{dic2},{dic3} is {result}")
