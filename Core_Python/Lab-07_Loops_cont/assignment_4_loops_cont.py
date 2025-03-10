#Q4. Python program to get the Fibonacci series between 0 to 50

# Initialize the first two numbers of the Fibonacci series
first_num=0
second_num=1

# Print the Fibonacci series between 0 and 50
print("The Fibonacci series between 0 to 50")

# Print the first two numbers of the series
print(f"{first_num}\n{second_num}")

# Generate the next numbers in the Fibonacci series
next_num=first_num+second_num  # Third number in the series
while (next_num<50):
    first_num=second_num # Update first_num to the previous second_num
    second_num=next_num # Update second_num to the previous next_num
    next_num=first_num+second_num# Calculate the next number in the series
    print(second_num) # Print the current Fibonacci number

"""
OUTPUT:

The Fibonacci series between 0 to 50
0
1
1
2
3
5
8
13
21
34
"""
