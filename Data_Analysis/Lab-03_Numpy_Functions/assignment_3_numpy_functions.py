"""
3. Suppose you have a dataset containing customer data, and you want to split this data into two groups:
one group for customers who made a purchase in the last 30 days and
another group for customers who haven't made a purchase in the last 30 days.

Input:
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

Output:

Active Customers (Last Purchase <= 30 days ago):
[101 102 103 104 105]

Inactive Customers (Last Purchase > 30 days ago):
[106 107 108 109 110]
"""
import numpy as np

# Input data
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Split customers into active and inactive groups based on last purchase days
active_customers = customer_ids[last_purchase_days_ago <= 30]
inactive_customers = customer_ids[last_purchase_days_ago > 30]

# Output
print(f"Active Customers (Last Purchase <= 30 days ago):\n{active_customers}\n")
print(f"Active Customers (Last Purchase <= 30 days ago):\n{inactive_customers}")

"""
OUTPUT:

Active Customers (Last Purchase <= 30 days ago):
[101 102 103 104 105]

Active Customers (Last Purchase <= 30 days ago):
[106 107 108 109 110]

"""

#Another Soloution
"""
import numpy as np
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
dic={}
list1=[]
list2=[]
for i in range(len(last_purchase_days_ago)):
    dic[last_purchase_days_ago[i]]=customer_ids[i]

for key,value in dic.items():
    if key<=30:
        list1.append(value)
    else:
        list2.append(value)

print(np.array(list1))
print(np.array(list2))"""


