#Q3. Write a python program finding the factorial of a given number using a while loop. 

#Input
number=int(input("Enter the positive number: "))
n=number

#Logic(factorial of a given number using a while loop) and output
factorial=1
if(n==0):
    print(f"The factorial of {number}! = 1")
else:
    while(n>0):
        factorial=factorial*n
        n=n-1
    print(f"The factorial of {number}! = {factorial}")
