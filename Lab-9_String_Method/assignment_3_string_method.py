"""3. Write a Python program to count Uppercase, Lowercase, special character
and numeric values in a given string Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

Output: 

UpperCase : 5 

LowerCase : 18 

NumberCase : 5 

SpecialCase : 11 """

input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase=0
lowercase=0
numbers=0
special=0
for i in input_str:
    if(i.isupper()):
        uppercase=uppercase+1
    elif(i.islower()):
        lowercase=lowercase+1
    elif(i.isdigit()):
        numbers=numbers+1
    else:
        special=special+1

print(f"UpperCase = {uppercase} \nLowerCase = {lowercase} \nNumbers = {numbers} \nSpecial = {special}")
