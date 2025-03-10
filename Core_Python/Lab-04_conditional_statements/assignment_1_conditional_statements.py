#Q1. Python program to check leap year 

#Input: Declaring an integer variables named 'year_input'
year_input=int(input("Enter the Year: "))

# Logic: Check if the year is a leap year using the leap year rules
if(year_input%400==0 and year_input%100==0):
    # Year is divisible by 400 and Year is divisible by 100 then it is a leap year
    print(f"{year_input} is a leap year.")
elif(year_input%4==0 and year_input%100!=0):
    # Year is divisible by 4 and Year is not divisible by 100 then it is a leap year
    print(f"{year_input} is a leap year.")
else:
    # Year is not obeying leap year rules, it is not a leap year
    print(f"{year_input} is Not a leap year.")



"""
OUTPUT: Sample 1

Enter the Year: 2025
2025 is Not a leap year.

OUTPUT: Sample 2

Enter the Year: 2024
2024 is a leap year.
"""
