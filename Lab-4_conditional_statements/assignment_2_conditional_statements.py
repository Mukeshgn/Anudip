#Q2. Python Program to Find the Largest Among Three Numbers

#Input
number_1=int(input("Enter the number_1: "))
number_2=int(input("Enter the number_2: "))
number_3=int(input("Enter the number_3: "))

#Logic(Largest Among Three Numbers) and Output
if(number_1>number_2 and number_1>number_3):
    print(f"{number_1} is the Largest Among {number_1},{number_2} and {number_3} Numbers.")
elif(number_2>number_1 and number_2>number_3):
    print(f"{number_2} is the Largest Among {number_1},{number_2} and {number_3} Numbers.")
else:
    print(f"{number_3} is the Largest Among {number_1},{number_2} and {number_3} Numbers.")
