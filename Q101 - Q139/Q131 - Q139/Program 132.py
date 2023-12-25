""" Q.Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The
circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective areas
and perimeter (circumference).
For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.
Examples
circy = Circle(11)
circy.getArea()
  (i)Should return 380.132711084365
circy = Circle(4.44)
circy.getPerimeter()
  (ii)Should return 27.897342763877365
Notes
Round results up to the nearest integer. """


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        # Calculate and return the area of the circle
        return round(math.pi * self.radius**2)

    def getPerimeter(self):
        # Calculate and return the perimeter (circumference) of the circle
        return round(2 * math.pi * self.radius)


# Test cases
circy = Circle(11)
print(circy.getArea())
print(circy.getPerimeter())

print('\n')

circy = Circle(4.44)
print(circy.getArea())
print(circy.getPerimeter())
