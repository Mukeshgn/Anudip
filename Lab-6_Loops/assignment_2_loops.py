#Q2. Write a python program to check whether a number is palindrome or not

#Input
number=int(input("Enter the number: "))
n=number

#Logic(Reverse number)
reverse_number=0
while(n>0):
    digit=n%10
    reverse_number=reverse_number*10+digit
    n=n//10

#Logic( number is palindrome or not) and output
if(number==reverse_number):
    print(f"The Given {number} is palindrome")
else:
    print(f"The Given {number} is not a palindrome")
