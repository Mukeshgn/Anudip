"""Q5. A transport company charges the fare according to following table: 

Distance     Charges 

1-50           8 Rs./Km 

51-100         10 Rs./Km

 > 100         12 Rs/Km
"""

# Input: Declaring an float variables named 'distance_travelled'
distance_travelled=float(input("Enter the distance travelled in kilometers: "))

# Logic: Calculate the fare based on the distance
if(1<=distance_travelled<=50):
     # Fare is 8 Rs per km for distances between 1 and 50 km
    fare = 8*distance_travelled
elif(51<=distance_travelled<=100):
    # Fare is 10 Rs per km for distances between 51 and 100 km
    fare = 10*distance_travelled
elif(distance_travelled>100):
    # Fare is 12 Rs per km for distances greater than 100 km
    fare = 10*distance_travelled
else:
    # For invalid distance
    fare=0

# Display the total fare
print(f"The total fare for {distance_travelled} km is: Rs. {fare}")



"""
OUTPUT: Sample

Enter the distance travelled in kilometers: 45
The total fare for 45.0 km is: Rs. 360.0
"""
