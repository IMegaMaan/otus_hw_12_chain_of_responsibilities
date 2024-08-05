from adapters.meta_ import MetaAdapter
from objects import Area, UObject

__all__ = ("IGetArea",)


class IGetArea(metaclass=MetaAdapter):
    @staticmethod
    def get_obj_area(u_obj: UObject) -> list[Area]:
        """тут предположим, что заложена логика вычисления нахождения объекта в конкретной зоне"""
        return []
