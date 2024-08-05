from adapters import IMovableForward
from commands.abstract_ import AbstractCommand
from objects import Context, Vector

__all__ = ("MoveCommand",)


class MoveCommand(AbstractCommand):
    def __init__(self, context: Context, movable: IMovableForward) -> None:
        super().__init__(context)
        self.movable: IMovableForward = movable

    def execute(self) -> None:
        position: Vector = self.movable.get_position()
        velocity: Vector = self.movable.get_velocity()

        self.movable.set_position(Vector.plus(position, velocity))
