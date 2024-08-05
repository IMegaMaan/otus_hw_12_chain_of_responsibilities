from abc import ABC, abstractmethod
from typing import ClassVar, TypeVar

from adapters.meta_ import MetaAdapter
from objects import Context

AdapterType = TypeVar("AdapterType", bound=MetaAdapter)


class AbstractCommand(ABC):
    raise_error: ClassVar[Exception] = Exception

    def __init__(self, context: Context, *args, **kwargs) -> None:
        self._context: Context = context

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError("Not implemented execute method!")
