from abc import ABC, abstractmethod
import math

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing circle with radius {self.radius}")

    def get_area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing rectangle {self.width}x{self.height}")

    def get_area(self):
        return self.width * self.height

class Triangle(Drawable):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def draw(self):
        print(f"Drawing triangle with base {self.base} and height {self.height}")

    def get_area(self):
        return 0.5 * self.base * self.height

class Canvas:
    def draw_all(self, shapes):
        for shape in shapes:
            shape.draw()
            print(f"  Area: {shape.get_area():.2f}\n")

if __name__ == "__main__":
    canvas = Canvas()

    shapes = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Triangle(3.0, 8.0),
    ]

    canvas.draw_all(shapes)