from commands.abstract_ import AbstractCommand
from commands.empty import EmptyCommand
from objects import Context

__all__ = ("InjectCommand",)


class InjectCommand(AbstractCommand):
    __DEFAULT_COMMAND: type[AbstractCommand] = EmptyCommand

    def __init__(self, context: Context) -> None:
        super().__init__(context)
        self._command = context.pop("command", InjectCommand.__DEFAULT_COMMAND)

    def execute(self) -> None:
        self._command(self._context).execute()


if __name__ == "__main__":
    command = InjectCommand({})
    command.execute()
