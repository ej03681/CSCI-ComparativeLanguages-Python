class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return self.width * 2 + self.height * 2

def main():
    r1 = Rectangle(4, 40)
    r2 = Rectangle(3.5, 35.7)
    
    print("Rectangle 1 width: ", r1.getWidth())
    print("Rectangle 1 height: ", r1.getHeight())
    print("Rectangle 1 area: ", r1.getArea())
    print("Rectangle 1 perimeter: ", r1.getPerimeter())
    
    print("Rectangle 2 width: ", r2.getWidth())
    print("Rectangle 2 height: ", r2.getHeight())
    print("Rectangle 2 area: ", r2.getArea())
    print("Rectangle 2 perimeter: ", r2.getPerimeter())
main()