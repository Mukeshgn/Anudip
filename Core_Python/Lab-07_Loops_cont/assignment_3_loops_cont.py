#Q3. Python program to check if a given number is an Armstrong number

# Input: Get the number from the user
number=int(input("Enter the number: "))

# Initialize variables
temp_num=number  # Temporary variable to store the original number
digit_count=0 # Variable to store the count of digits in the number

# Count the number of digits in the given number
while(temp_num!=0):
    digit_count=digit_count+1
    temp_num=temp_num//10 # Reduce the number by one digit

# Armstrong number calculation
temp_num=number # Reuse the original number for calculations
armstrong_sum=0 # Variable to store the sum of the digits raised to the power of digit_count

# Calculate the sum of digits raised to the power of digit_count
while(temp_num!=0):
    digit=temp_num%10  # Extract the last digit
    armstrong_sum=armstrong_sum+digit**digit_count # Add the power of the digit to the sum
    temp_num=temp_num//10 # Remove the last digit

# Check if the original number equals the Armstrong sum
if(number==armstrong_sum):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")


"""
OUTPUT: Sample

Enter the number: 153
153 is an Armstrong number
"""
