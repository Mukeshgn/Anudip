"""Q4. Accept numbers using input() function until the user enters 0.
If user input 0 then break the while loop and display the sum of all the numbers
"""


# Initialize the total sum variable
total_sum=0

# Start an infinite loop to accept numbers
while(True):
    # Taking input from the user
    number=int(input("Enter the number: "))

    # Check if the input is 0, and break the loop if it is
    if(number==0):
        break

    # Add the input number to the total sum
    total_sum=total_sum+number

# Output the sum of all the numbers entered
print(f"The sum of all numbers is {total_sum}")


"""
OUTPUT: Sample

Enter the number: 10
Enter the number: 20
Enter the number: 30
Enter the number: 0
The sum of all numbers is 60
"""
