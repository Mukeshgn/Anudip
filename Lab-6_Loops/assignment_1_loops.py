#Q1. Write a python program to reverse a number using a while loop.

#Input
n=int(input("Enter the number: "))
number=n

#Logic(reverse a number using a while loop)
reversed_number=0
while(number>0):
    digit=number%10
    reversed_number=reversed_number*10+digit
    number=number//10

#Output
print(f"The Reverse number of {n} is {reversed_number}")  
    
