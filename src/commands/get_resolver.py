from typing import Any, TypeVar

from commands.abstract_ import AbstractCommand

__all__ = ("GetResolverIocCommand",)

_T = TypeVar("_T")


class GetResolverIocCommand(AbstractCommand):
    def execute(self) -> _T:
        from ioc import IoC

        context: Any = self._context
        context["type_def"]: type[_T] = context.pop("service_key")

        async def resolve_type() -> _T:
            return IoC.resolve("GetIoCCommand", context=context).execute()

        return resolve_type
