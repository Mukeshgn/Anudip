#Q2. Python Program to Find the Largest Among Three Numbers

# Input: Declaring an integer variables named 'first_number','second_number' and 'third_number'
first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
third_number=int(input("Enter the third number: "))

# Logic: Check which number is the largest among the three
if(first_number>second_number and first_number>third_number):
    # first_number is the largest
    print(f"{first_number} is the Largest Among {first_number},{second_number} and {third_number} Numbers.")
elif(second_number>first_number and second_number>third_number):
    # second_number is the largest
    print(f"{second_number} is the Largest Among {first_number},{second_number} and {third_number} Numbers.")
else:
    # third_number is the largest
    print(f"{third_number} is the Largest Among {first_number},{second_number} and {third_number} Numbers.")



"""
OUTPUT: Sample

Enter the first number: 10
Enter the second number: 20
Enter the third number: 15
20 is the Largest Among 10,20 and 15 Numbers.
"""
