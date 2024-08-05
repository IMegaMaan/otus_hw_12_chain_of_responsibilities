from queue import Queue
from threading import Thread
from typing import ClassVar

from conditions import DefaultHandleCondition
from conditions.abstract_ import AbstractHandleCondition

__all__ = ("StorageCondition",)


class StorageCondition:
    """We can change to punq in the future."""

    queues: ClassVar[dict[str, Queue]] = {}
    threads: ClassVar[list[Thread]] = []

    condition_strategies: ClassVar[dict[str, type[AbstractHandleCondition]]] = {}
    default_condition: ClassVar[type[AbstractHandleCondition]] = DefaultHandleCondition
