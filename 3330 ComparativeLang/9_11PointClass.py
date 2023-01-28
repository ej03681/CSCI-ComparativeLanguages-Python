class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    def __distance__(self, p1):
        return ((p1.getX() - self.__x)**2 + (p1.getY() - self.__y)**2)**.5
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def __isNearBy__(self, p1):
        if self.__distance__(p1) < 5:
            print("The two points are near each other")
        else:
            print("The two points are not near each other")

def main():
    x1 = float(input("Enter the x-coordinate of point1 "))
    y1 = float(input("Enter the y-coordinate of point1 "))
    
    p1 = Point(x1, y1)
    
    x2 = float(input("Enter the x-coordinate of point2 "))
    y2 = float(input("Enter the y-coordinate of point2 "))
    
    p2 = Point(x2, y2)
    
    print("The distance between the two points is ", p1.__distance__(p2))
    p1.__isNearBy__(p2)
main()