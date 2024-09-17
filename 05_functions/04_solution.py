import math


def getAreaAndCirm(r):
    area = math.pi * r ** 2
    cirm = 2 * math.pi * r
    return math.floor(area), math.floor(cirm)


area, cirm = getAreaAndCirm(3)

print("Area: ", area, "Circumference: ", cirm)
