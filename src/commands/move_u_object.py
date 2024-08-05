from adapters import IMovableForward
from commands.abstract_ import AbstractCommand
from objects import Vector

__all__ = ("MoveCommand",)


class MoveCommand(AbstractCommand):
    def __init__(self, movable: IMovableForward) -> None:
        self.movable: IMovableForward = movable

    def execute(self) -> None:
        position: Vector = self.movable.get_position()
        velocity: Vector = self.movable.get_velocity()

        self.movable.set_position(Vector.plus(position, velocity))
