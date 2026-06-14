from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def get_area(self) -> float:
        return self._width * self._height


class Square(Shape):
    def __init__(self, side: float):
        self._side = side

    def get_area(self) -> float:
        return self._side * self._side


if __name__ == "__main__":
    rectangle: Shape = Rectangle(5, 10)
    square: Shape = Square(5)

    print(f"Rectangle area: {int(rectangle.get_area())}")
    print(f"Square area: {int(square.get_area())}")