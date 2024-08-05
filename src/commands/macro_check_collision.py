from adapters import IRotateArea
from commands.abstract_ import AbstractCommand
from commands.check_location import CheckLocationCommand
from commands.rotate_intersection import RotateUObjectIntersectionCommand

__all__ = ("CheckCollisionMacroCommand",)


class CheckCollisionMacroCommand(AbstractCommand):
    def execute(self) -> None:
        CheckLocationCommand(self._context).execute()
        RotateUObjectIntersectionCommand(self._context, IRotateArea()).execute()
