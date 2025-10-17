class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    @property
    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 5)
print(rectangle.length)     # 4
print(rectangle.width)      # 5
print(rectangle.perimeter)  # 18
print(rectangle.area)       # 20

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)     # 2
print(rectangle.width)      # 3
print(rectangle.perimeter)  # 10
print(rectangle.area)       # 6
