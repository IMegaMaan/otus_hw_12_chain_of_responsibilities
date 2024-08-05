from adapters.i_rotate_area import IRotateArea
from commands.abstract_ import AbstractCommand
from objects import Area, Context, Coordinate

__all__ = ("RotateUObjectIntersectionCommand",)


class RotateUObjectIntersectionCommand(AbstractCommand):
    """Если объект попал в новую окрестность, то удаляет его из списка объектов старой окрестности и добавляет
    список объектов новой окрестности.
    """

    def __init__(
        self,
        context: Context,
        i_rotate_area: IRotateArea,
        new_coordinates: Coordinate,
        old_areas: list[Area],
    ) -> None:
        super().__init__(context)
        self.__i_rotate_area = i_rotate_area
        self.__new_coordinates = new_coordinates
        self.__old_areas: list[Area] = old_areas

    def execute(self) -> None:
        old_areas: list[Area] = ...  # TODO тут ссылки на предыдущие окрестности приходят извне
        new_areas: list[Area] = ...  # TODO нужно по координатам получить новые зоны
        self.__i_rotate_area.change_areas(new_areas)
