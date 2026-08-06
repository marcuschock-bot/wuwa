#Inheritance
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.142 * (self.radius ** 2)
class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
    def area(self):
        return self.side * self.side

circle = Circle(5)
square = Square(4)

print(circle.name)
print(square.name)

#Polymorphism
def print_area(shape):
    print (f"{shape.name} area: {shape.area()}")

print_area(circle)
print_area(square)

shapes = [Circle(3), Square(5), Circle(2)]
for shape in shapes:
    print_area(shape)
