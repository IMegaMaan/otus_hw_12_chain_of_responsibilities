from adapters.meta_ import MetaAdapter
from objects import Area, UObject

__all__ = ("IRotateArea",)


class IRotateArea(metaclass=MetaAdapter):
    @staticmethod
    def change_areas(old_areas: list[Area], areas: list[Area], u_object: UObject):
        for old_area in old_areas:
            old_area.remove_object(u_object)

        for area in areas:
            area.add_object(u_object)
