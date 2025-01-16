"""Q2. Write a Python program to remove a newline in Python 

String = "\nBest \nDeeptech \nPython \nTraining\n"
"""
input_str="\nBest \nDeeptech \nPython \nTraining\n"
list_1=input_str.split("\n")
result=""
for word in list_1:
    result=result+word+" "
print(result.strip())
