import math
class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    def getPerimeter(self):
        return self.__side * self.__n
    def getArea(self):
        return (self.__n * (self.__side ** 2)) / (4 * math.tan(math.pi / self.__n))
def main():
    RP1 = RegularPolygon()
    RP2 = RegularPolygon(6, 4)
    RP3 = RegularPolygon(10, 4, 5.6, 7.8)
    
    print("Polygon 1 perimeter and area: ", RP1.getPerimeter(), ",", RP1.getArea())
    print("Polygon 2 perimeter and area: ", RP2.getPerimeter(), ",", RP2.getArea())
    print("Polygon 3 perimeter and area: ", RP3.getPerimeter(), ",", RP3.getArea())


main()