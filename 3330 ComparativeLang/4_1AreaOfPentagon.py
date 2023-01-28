import math 

numberOfSides = int(input("Enter the number of sides: "))
sideLength = float(input("Enter the side: "))

area = (numberOfSides * (sideLength ** 2)) / (4 * math.tan(math.pi / numberOfSides))

print("The area of the polygon is ", area)