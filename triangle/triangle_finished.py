from math import sqrt
from typing import Any


class PointProto:
    """Point class prototype"""
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
    
    def __str__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'
    

class Point(PointProto):
    """Point class"""
    def __init__(self, x: int, y: int):
        PointProto.__init__(self, x, y)

    def __str__(self) -> Any:
        return super().__str__()
    
    def get_distance(self, other: PointProto) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Triangle(object):
    """Triangle object"""
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__()
        self.a, self.b, self.c = a, b, c

    def __str__(self) -> Any:
        return f'{self.__class__.__name__}[{self.a}, {self.b}, {self.c}]'

    def get_perimeter(self) -> float:
        perimeter = self.a.get_distance(self.b) + \
            self.b.get_distance(self.c) + self.c.get_distance(self.a)

        return perimeter