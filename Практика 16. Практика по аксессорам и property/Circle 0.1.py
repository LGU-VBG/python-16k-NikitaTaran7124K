from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2
        self._area = pi * value ** 2

    @property
    def diameter(self):
        return self._diameter

    @property
    def area(self):
        return self._area

circle1 = Circle(1)
print(circle1.radius)        # 1
print(circle1.diameter)      # 2
print(round(circle1.area))   # 3

circle2 = Circle(5)
print(circle2.radius)        # 5
print(circle2.diameter)      # 10
print(round(circle2.area))   # 79

