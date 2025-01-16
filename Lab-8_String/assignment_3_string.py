"""Q3. Write a Python program to reverse words in a string 

String = “Deeptech Python Training”
"""
input_str="Deeptech Python Training"
list_1=input_str.split(" ")
result=""
for word in list_1:
    result=result+word[::-1]+" "
print(result.strip())
