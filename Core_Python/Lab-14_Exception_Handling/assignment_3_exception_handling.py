"""
3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
"""

try:
    # Decalring a String Variable with name "file_path"
    file_path=input("Enter the file path to read content: ")
    # Attempt to open file in read mode
    with open(file_path,'r') as file:
        # Read the content of the file
        content = file.read()
        # Display the content of the file
        print(content)


except FileNotFoundError:
    #Handle the case when the file is not found
    print("Error: The file '{file_path} does not exist.")

"""
OUTPUT: Sample 1

Enter the file path to read content: D:\\assignment_2_exception_handling.csv
Error: The file '{file_path} does not exist.

Sample 2

Enter the file path to read content: D:\\assignment_2_exception_handling.py
2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is notÂ aÂ validÂ integer

try:
    # Declaring a integer Variable with name 'user_input'
    user_input=input("Enter the Integer Value: ")
    # Attempt to convert the input to an integer
    user_input=int(user_input)
except ValueError:
    # Raise a ValueError exception if the input cannot be converted to an integer
    print("Error: Invalid input! Please enter a valid integer.")
else:
    # Diplaying the valid integer input if no exception occurs
    print(f"You entered a valid integer: {user_input}")


OUTPUT: Sample 1

Enter the Integer Value: 5
You entered a valid integer: 5


Sample 2

Enter the Integer Value: Anudip
Error: Invalid input! Please enter a valid integer.

"""
