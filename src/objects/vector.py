import math
from fractions import Fraction
from typing import Self

__all__ = ("Vector",)


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    @classmethod
    def plus(cls, position: Self, velocity: Self) -> Self:
        new_x: int = position.x + velocity.x
        new_y: int = position.y + velocity.y

        return Vector(new_x, new_y)

    def is_in_move(self) -> bool:
        return bool(self.x > 0 or self.y > 0)

    def get_module(self) -> Fraction:
        return Fraction(math.sqrt(self.x**2 + self.y**2))
