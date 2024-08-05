from typing import Any, TypeVar, cast

from commands.abstract_ import AbstractCommand

__all__ = ("GetIoCCommand",)

_T = TypeVar("_T")


class GetIoCCommand(AbstractCommand):
    def execute(self) -> _T:
        from ioc import IoC

        context: Any = self._context
        type_def: type[_T] = context.pop("type_def")

        return cast(_T, IoC.container.resolve(type_def, **context))
