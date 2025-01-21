"""Q1. Write a Python program and calculate the mean of the below dictionary.

test_dict={"A": 6, "B": 9, "C": 5, "D" : 7, "E" :4}

Output: 6.2
"""
#Input
test_dict={"A": 6, "B": 9, "C": 5, "D" : 7, "E" :4}

#Logic
mean=0
for val in test_dict.values():
    mean=mean+val
result=mean/len(test_dict)

#Output
print(f"The mean of {test_dict} dictionary is {result}")
