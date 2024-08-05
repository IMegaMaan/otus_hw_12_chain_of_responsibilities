from commands.abstract_ import AbstractCommand

__all__ = ("CheckCollisionMacroCommand",)


# TODO нужно реализовать
class CheckCollisionMacroCommand(AbstractCommand):
    def execute(self) -> None:
        # 1. проверка, изменился ли location
        # 2. изменение принадлежности к Area при необходимости
        RotateUObjectIntersectionCommand()
        # 3. Что-то еще?
