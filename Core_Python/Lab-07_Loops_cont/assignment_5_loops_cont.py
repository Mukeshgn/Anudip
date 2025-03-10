#Q5. Python program to check the validity of password input by users

"""
Primary conditions for password validation:

Minimum 8 characters.
The alphabet must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ]."""

# Input: Get the password from the user
password=input("Enter the Password: ")

# Define the required character sets
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
special_characters="_@$"

lowercase_count=0
uppercase_count=0
digits_count=0
special_characters_count=0

# Check password length
if(len(password)>=8):
    # Iterate over each character in the password to check the conditions
    for char in password:
        if(char in lowercase_letters):
            lowercase_count=lowercase_count+1
        elif(char in uppercase_letters):
            uppercase_count=uppercase_count+1
        elif(char in digits):
            digits_count=digits_count+1
        elif(char in special_characters):
            special_characters_count=special_characters_count+1
    
else:
    print("Enter the password with minimum 8 characters")

# Check if all conditions are met
if(lowercase_count<1 or uppercase_count<1 or digits_count<1 or special_characters_count<1):
    print(f"{password} is invalid")
else:
    print(f"{password} is valid")


"""
OUTPUT: Sample 1

Enter the Password: Anudip123@
Anudip123@ is valid

Sample 2

Enter the Password: Anudip
Enter the password with minimum 8 characters
Anudip is invalid
"""

    


