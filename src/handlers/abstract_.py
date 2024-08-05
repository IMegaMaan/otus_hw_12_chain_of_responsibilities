from abc import ABC, abstractmethod
from queue import Queue
from typing import Any

from commands import AbstractCommand

__all__ = (
    "AbstractHandler",
    "AbstractErrorHandler",
)


class AbstractHandler(ABC):
    @abstractmethod
    def handle(self, *args, **kwargs):
        raise NotImplementedError


class AbstractErrorHandler(ABC):
    def __init__(self, *, command: type[AbstractCommand], error: Exception, queue: Queue, **kwargs: Any) -> None:
        self.command: type[AbstractCommand] = command
        self.error: Exception = error
        self.queue: Queue = queue
        self.kwargs: Any = kwargs

    @abstractmethod
    def execute(self) -> None: ...
