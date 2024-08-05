from typing import ClassVar

from adapters import IMovableForward
from adapters.intersection import IGetArea
from commands.abstract_ import AbstractCommand
from commands.exceptions import ChangedAreaError
from objects import Area, Context, Vector

__all__ = ("CheckUObjectAreaCommand",)


class CheckUObjectAreaCommand(AbstractCommand):
    """Определяет окрестность, в которой присутствует игровой объект.
    - Реализация сейчас не требуется. Будем считать, что заложена некоторая логика.
    - если объект попал в новую окрестность, то удаляет его из списка объектов старой окрестности и добавляет
    список объектов новой окрестности.
    - для каждого объекта новой окрестности и текущего движущегося объекта создает команду проверки коллизии этих
    двух объектов. Все эти команды помещает в макрокоманду и эту макрокоманду записывает на место
    аналогичной макрокоманды для предыдущей окрестности.
    """

    raise_error: ClassVar[Exception] = ChangedAreaError

    def __init__(self, context: Context, i_intersection: IGetArea, i_movable: IMovableForward) -> None:
        super().__init__(context)
        self._i_intersection = i_intersection
        self._i_movable = i_movable

    def execute(self) -> None:
        old_areas: list[Area] = self._i_intersection.get_obj_current_areas(self._context["u_object"])
        position: Vector = self._i_movable.get_position()
        get_eras_by_location: list[Area] = self._i_intersection.get_obj_areas_by_location(
            self._context["u_object"], position,
        )

        if not self.__is_the_same_location(old_areas, get_eras_by_location):
            raise CheckUObjectAreaCommand.raise_error("Location Changed.")

    def __is_the_same_location(self, old_locations: list[Area], new_locations: list[Area]) -> bool:
        return old_locations == new_locations
