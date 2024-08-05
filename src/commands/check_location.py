from commands import AbstractCommand

__all__ = ("CheckLocationCommand",)


class CheckLocationCommand(AbstractCommand):
    def execute(self) -> None:
        # some logic to check location
        ...
