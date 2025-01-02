#Q2. Using input function take two number and then swap the number 

#Input
number_1=int(input("Enter the number: "))
number_2=int(input("Enter the number: "))

#Before Swapping
print(f"Before Swapping: number_1 = {number_1} and number_2 = {number_2}.")

#Logic(After swap the number)
number_1,number_2=number_2,number_1

#Output
print(f"After Swapping: number_1 = {number_1} and number_2 = {number_2}.")
