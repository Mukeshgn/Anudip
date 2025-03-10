#Q3. Python Program to Check if a Number is Positive, Negative or 0 


# Input: Declaring an integer variables named 'number'
number=int(input("Enter the Number: "))

# Logic: Check if the number is positive, negative, or zero
if(number==0):
    # Number is zero
    print(f"The Given Number {number} is Zero.")
elif(number>0):
    # Number is positive
    print(f"The Given Number {number} is Positive.")
else:
    # Number is negative
    print(f"The Given Number {number} is Negative.")



"""OUTPUT: Sample

Enter the Number: -6
The Given Number -6 is Negative.
"""
