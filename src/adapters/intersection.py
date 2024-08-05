from adapters.meta_ import MetaAdapter
from objects import Area, UObject, Vector

__all__ = ("IGetArea",)


class IGetArea(metaclass=MetaAdapter):
    @staticmethod
    def get_obj_current_areas(u_obj: UObject) -> list[Area]:
        """тут предположим, что заложена логика вычисления нахождения объекта в конкретной зоне"""
        return []

    @staticmethod
    def get_obj_areas_by_location(u_obj: UObject, location: Vector) -> list[Area]:
        """тут предположим, что заложена логика вычисления нахождения объекта в конкретной зоне"""
        return []
