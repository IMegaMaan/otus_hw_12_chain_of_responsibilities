from typing import ClassVar

from commands.abstract_ import AbstractCommand
from handlers.abstract_ import AbstractErrorHandler

__all__ = ("ExceptionHandler",)


class ExceptionHandler:
    """Example of use:
    _STORE: ClassVar[dict] = {
        CommandLogInformation: {
            LogInformationError: ErrorHandlerPutQueueLog,
        },
        CommandRepeat: {
            RepeatError: HandlerRepeatToQueue,
        },
        # для пункта 8
        MultiCommandFourSix: {
            FirstMultiCommandError: HandlerRepeatToQueue,  # повтор
            RepeatError: ErrorHandlerPutQueueLog,  # лог
        },
        # для 9
        SomeCommandForDoubleRepeatAndLog: {
            DoubleRepeatLogError: FirstHandlerRepeatToQueue,
            FirstRepeatError: HandlerRepeatToQueue,
            RepeatError: ErrorHandlerPutQueueLog,
        },
    }


    """

    _STORE: ClassVar[dict] = {}

    @staticmethod
    def handle(command: AbstractCommand, exception: Exception) -> type[AbstractErrorHandler]:
        type_command: type[AbstractCommand] = type(command)
        type_exception: type[Exception] = type(exception)

        return ExceptionHandler._STORE[type_command][type_exception]
