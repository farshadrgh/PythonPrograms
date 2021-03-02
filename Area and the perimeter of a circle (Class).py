class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


Our_Circle = Circle(12)
print("Circle area is : {}".format(Our_Circle.area()))
print("Circle perimeter is : {}".format(Our_Circle.perimeter()))
