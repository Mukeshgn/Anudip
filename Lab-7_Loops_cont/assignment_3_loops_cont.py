#Q3. Python program to check if a given number is an Armstrong number

#Input
num=int(input("Enter the number: "))

#count of numbers
number_1=num
count=0
while(number_1!=0):
    count=count+1
    number_1=number_1//10

#Logic(Armstrong)
number_2=num
result=0
while(number_2!=0):
    digit=number_2%10
    result=result+digit**count
    number_2=number_2//10

#Output
if(num==result):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")


