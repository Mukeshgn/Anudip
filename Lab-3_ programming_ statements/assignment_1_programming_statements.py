#Q1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

#Input
number=int(input("Enter the Number: "))

#Logic(using ternary operators check whether the number is even or odd)
even_or_odd="Even" if number%2==0 else "Odd"

#Output
print(f"The Given number {number} is {even_or_odd}.")
