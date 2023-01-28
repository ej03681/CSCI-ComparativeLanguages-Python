a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b ** 2 - 4 * a * c
r1 = (-b + discriminant ** .5) / (2 * a)
r2 = (-b - discriminant ** .5) / (2 * a)

if discriminant > 0 :
    print("The roots are ", r1, " and ", r2)
elif discriminant == 0 :
    print("The root is ", r1)
else: 
    print("The equation has no real roots")