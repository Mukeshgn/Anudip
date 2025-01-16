"""1. Write a Python program to Count all letters, digits, and special symbols from the given string 

Input = “P@#yn26at^&i5ve” 

Output: Chars = 8 Digits = 2 Symbol = 3 """

input_str = "P@#yn26at^&i5ve"
alpha=0
digits=0
symbol=0

for i in input_str:
    if(i.isalpha()):
        alpha=alpha+1
    elif(i.isdigit()):
        digits=digits+1
    else:
        symbol=symbol+1

print(f"Chars = {alpha} Digits = {digits} Symbols={symbol}")
        
