# Recommend a type of pet food based on the pet's species and age. (e.g.,
#  Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
species = input("Enter pet's species:")
petAge = int(input("Enter Dog Age:"))

if species == "Dog":
    if petAge < 2:
        print("Puppy food")
    else:
        print("Senior dog food")
elif species == "Cat":
    if petAge > 5:
        print("Senior cat food")
    else:
        print("Cat food")
