age = int(input("Enter the age: "))
day = input("Enter the Day: ")

price = 12 if age >= 18 else 8
if (day == "Wednesday"):
    price -= 2


if (age >= 18):
    print(price)
else:
    print(price)
