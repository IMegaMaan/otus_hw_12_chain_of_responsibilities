from typing import TYPE_CHECKING, Any, TypeVar

import punq

from commands.abstract_ import AbstractCommand

if TYPE_CHECKING:
    from collections.abc import Callable

__all__ = ("RegisterIoCCommand",)

_T = TypeVar("_T")


class RegisterIoCCommand(AbstractCommand):
    def execute(self) -> None:
        from ioc import IoC

        context: Any = self._context

        service_key: type[_T] = context.pop("register_service_key")
        factory: Callable[..., _T] | punq._Empty = context.pop("factory", punq.empty)
        instance: _T | punq._Empty = context.pop("instance", punq.empty)

        IoC.container.register(service_key, factory=factory, instance=instance, **context)
