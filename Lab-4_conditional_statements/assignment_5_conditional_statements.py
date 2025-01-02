"""Q5. A transport company charges the fare according to following table: 

Distance     Charges 

1-50             8 Rs./Km 

51-100         10 Rs./Km

 > 100           12 Rs/Km
"""

#Input
distance=float(input("Enter the distance travelled in kilometers: "))

#Logic
if(1<=distance<=50):
    fare = 8*distance
elif(51<=distance<=100):
    fare = 10*distance
elif(distance>100):
    fare = 10*distance
else:
    fare=0

#Output
print(f"The total fare for {distance} km is: Rs. {fare}")
