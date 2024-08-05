from collections import namedtuple
from functools import lru_cache
from uuid import uuid4

from objects.exceptions import WrongInstance
from objects.uobj import UObject

__all__ = (
    "Area",
    "BattleField",
    "Coordinate",
)

Coordinate: namedtuple = namedtuple("Coordinate", ["x", "y"])


class Area:
    """Класс, представляющий собой сущность окрестностей, в которых находится объект"""

    def __init__(self, x: int, y: int, length: int = 4, height: int = 4):
        """Конструктор.

        :param x: координата по оси x
        :param y: координата по оси y
        :param length: длина окрестности, от координаты x вправо
        :param height: высота окрестности, от координаты y вверх
        """
        self._x = x
        self._y = y
        self._length = length
        self._height = height
        self._objects: set = set()
        self.__uuid = str(uuid4())

    def add_object(self, obj: UObject) -> None:
        if not isinstance(obj, UObject):
            raise WrongInstance("Wring type of instance to add!")
        self._objects.add(obj)

    def remove_object(self, obj: UObject) -> None:
        if not isinstance(obj, UObject):
            raise WrongInstance("Wring type of instance to remove!")
        self._objects.remove(obj)

    def all_objects_in(self) -> list[UObject]:
        return [u_object for u_object in self._objects]


class BattleField:
    """Игровой объект, размер игрового поля. Вычисляет необходимое число перекрестков для игрового поля.
    Структура данных, формируемая для игрового поля, фактически, сетка:
    [
    [0,1,2,3],
    [0,1,2,3],
    [0,1,2,3],
    [0,1,2,3]
    ]
    Тут первый индекс это ось y, второй, ось x
    area = [0][1], по это ссылке получаем зону 0, 1 для y = 0 и для x = 1, где это не координаты, а порядок хранения
    самих зон или сеток.

    """

    def __init__(self, x: int, y: int, count_areas: int = 16) -> None:
        """:param x: размер игрового поля в единицах измерения по оси x
        :param y: размер игрового поля в единицах измерения по оси y
        :param count_areas: количество окрестностей, на которое будет разделено поле.
        """
        self._x: int = x
        self._y: int = y
        self._count_intersections: int = count_areas
        self._areas: list[list[Area]] = self.__create_areas()

    def __create_areas(self) -> list[list[Area]]:
        """Создание необходимого количества окрестностей для игрового поля."""
        x_current: int = 0
        y_current: int = 0

        per_x_axis = self._count_intersections // self._x
        per_y_axis = self._count_intersections // self._y

        areas: list = [None] * per_y_axis
        for y_count in range(per_y_axis):
            x_axis = [] * per_x_axis
            for x_count in range(per_x_axis):
                intersection_instance = Area(x_current, y_current)
                x_axis.append(intersection_instance)
                x_current += per_x_axis
            areas[y_count] = x_axis
            y_current += per_y_axis
            x_current = 0

        return areas

    def get_area_by_uuid(self, coordinate: Coordinate) -> Area | None:
        """Возвращает объект перекрестка по `id` или None, если такого перекрестка не существует."""
        return self._areas[coordinate.y][coordinate.x]

    # TODO фактически, это метод адаптера на определение пересечений.
    def get_area_by_coordinates(self, x: int, y: int) -> list[Area]:
        """Получение зоны по входящим x и y координатам сетки. В приграничных условиях, т.е. когда дается координата,
        принадлежащая сразу двум сеткам, например, x=4, y=4, возвращаться буду все координатные сетки.

        """
        # 1 вычисляем, каким зонам принадлежат координаты
        x_step = self._count_intersections // self._x
        y_step = self._count_intersections // self._y

        full_x, rest_x = divmod(x, x_step)
        full_y, rest_y = divmod(y, y_step)

        # если остаток по какой-то остаток 0, то значит находимся в двух зонах сразу

        # если остаток есть, то к текущей позиции координаты прибавляем еще 1 и получаем актуальный индекс

        return ...

    @lru_cache
    def get_all_areas(self) -> list[list[Area]]:
        return self._areas


if __name__ == "__main__":
    battle_field = BattleField(x=4, y=4)
    battle_field.get_all_areas()
