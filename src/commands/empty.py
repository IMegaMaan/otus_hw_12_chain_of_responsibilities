from commands.abstract_ import AbstractCommand

__all__ = ("EmptyCommand",)


class EmptyCommand(AbstractCommand):
    def execute(self) -> None:
        return
