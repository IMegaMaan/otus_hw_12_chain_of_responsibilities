from adapters.i_rotate_area import IRotateArea
from commands.abstract_ import AbstractCommand
from objects import Area, Context

__all__ = ("RotateUObjectIntersectionCommand",)


class RotateUObjectIntersectionCommand(AbstractCommand):
    """Если объект попал в новую окрестность, то удаляет его
    из списка объектов старой окрестности и добавляет
    список объектов новой окрестности.
    """

    def __init__(
        self,
        context: Context,
        i_rotate_area: IRotateArea,
    ) -> None:
        super().__init__(context)
        self._i_rotate_area = i_rotate_area
        self._new_coordinates = context.pop("new_coordinates", [])
        self._old_areas: list = context.pop("old_areas", [])

    def execute(self) -> None:
        old_areas: list[Area] = []
        new_areas: list[Area] = []
        self._i_rotate_area.change_areas(old_areas, new_areas, self._context["u_object"])
