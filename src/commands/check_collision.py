from typing import ClassVar

from adapters import ICollision
from commands.abstract_ import AbstractCommand
from commands.exceptions import CollisionError
from objects import Context, UObject

__all__ = ("CheckCollisionCommand",)


class CheckCollisionCommand(AbstractCommand):
    raise_error: ClassVar[Exception] = CollisionError

    def __init__(self, context: Context, i_collision: ICollision, one_u_obj: UObject, second_u_obj: UObject) -> None:
        super().__init__(context)
        self._i_collision = i_collision
        self._one_u_obj = one_u_obj
        self._second_u_obj = second_u_obj

    def execute(self) -> None:
        is_has_collision = self._i_collision.check_collision(self._one_u_obj, self._second_u_obj)

        if is_has_collision:
            raise CheckCollisionCommand.raise_error(
                f"Objects: {self._one_u_obj} and {self._second_u_obj} has collision!",
            )
