class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self, side1 = 1, side2 = 1, side3 = 1):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return (s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)) ** .5
    
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + "side2 = " + str(self.__side2) + "side3 = " + str(self.__side3)
    
def main():
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))
    
    triangle1 = Triangle(side1, side2, side3)
    
    color = input("Enter color: ")
    
    fill = int(input("Enter 1/0 for filled (1: true, 0: false): "))
    isFilled = (fill == 1)
    
    triangle1.setColor(color)
    triangle1.setFilled(isFilled)

    
    print("The area is ", triangle1.getArea())
    print("The perimeter is ", triangle1.getPerimeter())
    print("Color is ", triangle1.getColor())
    print("Fill is ", triangle1.isFilled())
    
main()