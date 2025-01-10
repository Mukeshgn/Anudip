#Q2. Python program to check if the given string is a palindrome

#Input
string=input("Enter the String: ")

#Revers the String
reverse_string=""
for i in string:
    reverse_string=i+reverse_string

#Logic(palindrome) and Output
if(string==reverse_string):
    print(f"{string} is a Palindrome")
else:
    print(f"{string} is not a Palindrome")
