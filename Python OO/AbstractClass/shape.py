from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_square_meter(self):
        pass

    def __str__(self):
        return f"Your shape as a surface of: {self.calculate_square_meter()} m²"

class Square(Shape):
    def __init__(self, side):
        self._side = side

    def calculate_square_meter(self):
        return self._side * self._side

class Rectangle(Shape):
    def __init__(self, large_side, long_side):
        self._large_side = large_side
        self._long_side = long_side

    def calculate_square_meter(self):
        return self._long_side * self._large_side


c = Square(5)
print(c)
r = Rectangle(5,6)
print(r)