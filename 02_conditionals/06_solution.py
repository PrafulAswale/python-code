distance = int(input("Enter distance in km:"))
Transportation_Mode = ""

if distance < 3:
    Transportation_Mode = "Walk"
elif distance >= 3 and distance <= 15:
    Transportation_Mode = "Bike"
else:
    Transportation_Mode = "Car"

print(Transportation_Mode)
