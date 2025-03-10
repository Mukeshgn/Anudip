'''Q4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders
for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is
given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys,
and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is
required to pay after the discount. '''


# Input: Declaring an integer variables named 'product_code' and 'order_amount'

product_code=int(input("Product code:\n 1 for Battery Based Toys\n 2 for Key-based Toys\n 3 for Electrical Charging Based Toys\n Enter the product code: "))
order_amount=int(input("Enter the order amount: "))

# Logic: Determine the discount based on the product code and order amount
discount=0

if(product_code==1):
    # Battery-based toys: 10% discount for orders above Rs. 1000
    if(order_amount>1000):
        discount=0.10*order_amount
elif(product_code==2):
    # Key-based toys: 5% discount for orders above Rs. 100
    if(order_amount>100):
        discount=0.05*order_amount
elif(product_code==3):
    # Electrical charging-based toys: 10% discount for orders above Rs. 500
    if(order_amount>500):
        discount=0.10*order_amount
else:
    # Invalid product code
    print("Invalid Produvt Code")
    exit()

# Calculate the net amount after applying the discount
net_amount=order_amount-discount

# Display the net amount the customer has to pay
print(f" The net amount that the customer is required to pay after the discount is Rs. {net_amount}")



"""
OUTPUT: Sample

Product code:
 1 for Battery Based Toys
 2 for Key-based Toys
 3 for Electrical Charging Based Toys
 Enter the product code: 1
Enter the order amount: 1200
 The net amount that the customer is required to pay after the discount is Rs. 1080.0
 """
