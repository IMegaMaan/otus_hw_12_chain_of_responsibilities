from adapters.meta_ import MetaAdapter
from objects import UObject

__all__ = ("ICollision",)


class ICollision(metaclass=MetaAdapter):
    @staticmethod
    def check_collision(first_u_obj: UObject, second_u_obj: UObject) -> bool:
        # some logic here to check collision
        return False
