from abc import ABC, abstractmethod
from queue import Queue
from typing import TYPE_CHECKING, Any

from commands import AbstractCommand

if TYPE_CHECKING:
    from collections.abc import Hashable


class AbstractHandleCondition(ABC):
    QUEUE_TASK_GET_TIMEOUT = 1

    def __init__(self, queue: Queue, thread_id: int) -> None:
        self._queue = queue
        self._thread_id = thread_id
        self._command_class: type[AbstractCommand] | None = None
        self._kwargs: dict[Hashable, Any] = {}
        self._current_command: AbstractCommand | None = None
        self._error: Exception | None = None

    @abstractmethod
    def run_thread(self) -> bool: ...

    @abstractmethod
    def handle(self) -> None: ...
