#Q5. Python program to check the validity of password input by users

"""
Primary conditions for password validation:

Minimum 8 characters.
The alphabet must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ]."""

#Input
password=input("Enter the Password: ")

#Logic(Password validity) and output
lower_alphabet="abcdefghijklmnopqrstuvwxyz"
upper_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
character="_@$"

l=0
u=0
n=0
c=0

if(len(password)>=8):
    for i in password:
        if(i in lower_alphabet):
            l=l+1
            print(l)
        elif(i in upper_alphabet):
            u=u+1
            print(u)
        elif(i in number):
            n=n+1
            print(n)
        elif(i in character):
            c=c+1
            print(c)
    
else:
    print("Enter the password with minimum 8 characters")

if(l<1 or u<1 or n<1 or c<1):
    print(f"{password} is invalid")
else:
    print(f"{password} is valid")


    


