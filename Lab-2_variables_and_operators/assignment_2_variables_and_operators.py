#Q2. Declare two variables and print that which variable is largest using ternary operators 

#input
variable_1=int(input("Enter the Number for variable_1 : "))
variable_2=int(input("Enter the Number for variable_2 : "))

#Logic(largest number using ternary operation)
largest="variable_1" if variable_1> variable_2 else "variable_2"

#output
print(largest,"is the largest variable")
