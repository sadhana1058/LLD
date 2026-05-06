# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     def __init__(self, name: str):
#         self._name = name

#     @abstractmethod
#     def area(self) -> float:
#         pass

#     @abstractmethod
#     def perimeter(self) -> float:
#         pass

#     def describe(self) -> None:
#         # Print: "Shape: [name], Area: [area], Perimeter: [perimeter]"
#         # Use f-string with :.2f for formatting
#         print(f"Shape: {self._name}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")
       

# class Circle(Shape):
#     def __init__(self, radius: float):
#         super().__init__("Circle")
#         self._radius = radius

#     def area(self) -> float:
#         Area = math.pi * self._radius**2
#         return Area

#     def perimeter(self) -> float:
#         Perimeter = 2 *math.pi * self._radius
#         return Perimeter

# class Rectangle(Shape):
#     def __init__(self, width: float, height: float):
#         super().__init__("Rectangle")
#         self._width = width
#         self._height = height

#     def area(self) -> float:
#         # Area = width * height
#         return self._width*self._height

#     def perimeter(self) -> float:
#         # Perimeter = 2 * (width + height)
#         return 2*(self._width+self._height)


# if __name__ == "__main__":
#     circle = Circle(5.0)
#     circle.describe()
#     print(circle.area())
#     print(circle.perimeter())
#     rectangle = Rectangle(4.0, 6.0)
#     rectangle.describe()
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self) -> None:
        # Print: "Shape: [name], Area: [area], Perimeter: [perimeter]"
        # Use f-string with :.2f for formatting
        print(f'Shape: {self._name}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}')
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self._radius = radius

    def area(self) -> float:
        Area = math.pi * self._radius**2
        return Area

    def perimeter(self) -> float:
        Perimeter = 2 *math.pi * self._radius
        return Perimeter

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self._width = width
        self._height = height

    def area(self) -> float:
        # Area = width * height
        return self._width*self._height

    def perimeter(self) -> float:
        # Perimeter = 2 * (width + height)
        return 2*(self._width+self._height)


if __name__ == "__main__":
    circle = Circle(5.0)
    circle.describe()

    rectangle = Rectangle(4.0, 6.0)