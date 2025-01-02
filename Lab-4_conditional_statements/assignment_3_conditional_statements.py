#Q3. Python Program to Check if a Number is Positive, Negative or 0 

#Input
number=int(input("Enter the Number: "))

#Logic(Number is Positive, Negative or 0) and Output
if(number==0):
    print(f"The Given Number {number} is 0.")
elif(number>0):
    print(f"The Given Number {number} is Positive.")
else:
    print(f"The Given Number {number} is Negative.")
