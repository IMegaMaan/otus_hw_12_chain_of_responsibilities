import logging

from commands import AbstractCommand
from conditions import AbstractHandleCondition
from handlers import AbstractErrorHandler, ExceptionHandler

__all__ = ("BaseHandleCondition",)

logger = logging.getLogger(__name__)


class BaseHandleCondition(AbstractHandleCondition):
    QUEUE_TASK_GET_TIMEOUT = 1

    def run_thread(self) -> bool:
        return True

    def _get_task(self) -> None:
        logger.info(f"Ждем таску в потоке {self._thread_id}")
        self._command_class, self._kwargs = self._queue.get(timeout=self.QUEUE_TASK_GET_TIMEOUT)
        self._queue.task_done()

    def run_command_try(self) -> None:
        current_command = self._get_current_command()
        current_command.execute()

    def _get_current_command(self) -> AbstractCommand | None:
        if self._command_class is None:  # when exception Queue Get happened
            return None
        elif self._current_command is None:  # noqa: RET505
            return self._command_class(queue=self._queue, **self._kwargs)
        return self._current_command

    def exception_catch(self) -> None:
        source_command: AbstractCommand = self._kwargs.get("source_command", self._get_current_command())
        self._kwargs["source_command"] = source_command
        handler_class: type[AbstractErrorHandler] = ExceptionHandler.handle(source_command, self._error)
        handler: AbstractErrorHandler = handler_class(
            command=self._command_class,
            error=self._error,
            queue=self._queue,
            **self._kwargs,
        )
        handler.execute()

    def handle(self) -> None:
        try:
            self._get_task()
            self.run_command_try()
        except Exception as error:  # noqa: BLE001
            self._error = error
            self.exception_catch()
