x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the x-coordinate of the point: "))

x = (x ** 2) ** .5
y = (y ** 2) ** .5

if x >= 10 / 2:
    print("Point (", x, ",", y, ") is not in the rectangle")
elif y >= 5.0 / 2:
    print("Point (", x, ",", y, ") is not in the rectangle")
else :
    print("Point (", x, ",", y, ") is in the rectangle")
