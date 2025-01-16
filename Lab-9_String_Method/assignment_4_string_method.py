""" 4. Write a Python Count vowels in a string 

input= “Welcome to Python Assignment” 

Output: Total vowels are: 8 """
input_str = "Welcome to Python Assignment"
# Output: Total vowels are: 8
count=0
vowels="aeiouAEIOU"
for i in input_str:
    if i in vowels:
        count=count+1
print(f"Total vowels are: {count}")
