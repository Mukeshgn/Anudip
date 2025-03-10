#Q2. Using input function take two number and then swap the number 


# Declaring an float variables named 'first_number' and 'second_number'
first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))

# Before Swapping: Display the numbers before they are swapped
print(f"Before Swapping: first number = {first_number} and second number = {second_number}.")

# Logic: Swap the values of the two numbers using tuple unpacking
first_number,second_number=second_number,first_number

# After Swapping: Display the numbers after they are swapped
print(f"After Swapping: first number = {first_number} and second number = {second_number}.")



"""
OUTPUT: Sample

Enter the first number: 5
Enter the second number: 10
Before Swapping: first number = 5 and second number = 10.
After Swapping: first number = 10 and second number = 5.
"""
