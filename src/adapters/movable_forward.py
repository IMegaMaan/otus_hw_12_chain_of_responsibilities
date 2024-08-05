from adapters.meta_ import MetaAdapter
from objects import Vector

__all__ = ("IMovableForward",)


class IMovableForward(metaclass=MetaAdapter):
    """Движение только по прямой."""

    def get_position(self) -> Vector:
        """Доступ к текущей позиции через объект, хранящий атрибуты и адаптер.

        :return: Vector(current_x, current_y)
        """
        raise NotImplementedError("Условно, реализация есть. Для тестов мокаем.")

    def set_position(self, new_value: Vector) -> None:
        raise NotImplementedError("Условно, реализация есть. Для тестов мокаем.")

    def get_velocity(self) -> Vector:
        """Вычисление через следующую формулу. Доступ к атрибутам через объект-посредник с атрибутами.

        x = v * cos(d/360*n)
        y = v * sin(d*360*n)

        :return: Vector(x, y)
        """
        raise NotImplementedError("Условно, реализация есть. Для тестов мокаем.")

    def set_velocity(self, new_value: Vector) -> None:
        raise NotImplementedError("Условно, реализация есть. Для тестов мокаем.")
