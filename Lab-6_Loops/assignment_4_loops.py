"""Q4. Accept numbers using input() function until the user enters 0.
If user input 0 then break the while loop and display the sum of all the numbers
"""


#Input and Logic
total=0
while(True):
    number=int(input("Enter the number: "))
    if(number==0):
        break
    total=total+number

#Output
print(f"The sum of all numbers is {total}")
