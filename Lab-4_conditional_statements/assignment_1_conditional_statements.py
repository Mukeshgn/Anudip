#Q1. Python program to check leap year 

#Input
year=int(input("Enter the Year: "))

#Logic(leap year)
if(year%400==0 and year%100==0):
    print(f"{year} is a leap year.")
elif(year%4==0 and year%100!=0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is Not a leap year.")
