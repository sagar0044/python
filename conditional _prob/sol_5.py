# Transportation mode selection.

distance=input("For the distance:")
distance=int(distance)

if distance<3:
    transport_mode="Walk"
elif distance<=15:
    transport_mode="Bike"
else:
    transport_mode="Car"

print("I recommend u the transportation mode through :",transport_mode)

