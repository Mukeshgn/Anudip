"""
Q4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
"""

try:
    # Declaring a integer variable named "first_number"
    first_number=int(input("Enter the first number: "))
    # Declaring a String variable named "second_number"
    second_number=input("Enter the second number: ")
    # Adding the integer variable and String variable to occur TypeError
    result=first_number+second_number
    # Displaying the result
    print(result)
                      
except TypeError as e:
    # Handle the case when two different type of variable cannot be add
    print("Error: Type Error Occured! ",e)


"""
OUTPUT: Sample

Enter the first number: 5
Enter the second number: 6
Error: Type Error Occured!  unsupported operand type(s) for +: 'int' and 'str'
"""
