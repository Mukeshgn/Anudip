#Q4. Python program to get the Fibonacci series between 0 to 50

num_1=0
num_2=1
num_3=1
print("The Fibonacci series between 0 to 50")
print(f"{num_1}\n{num_2}")
while (num_3<50):
    num_1=num_2
    num_2=num_3
    num_3=num_1+num_2
    print(num_2)
