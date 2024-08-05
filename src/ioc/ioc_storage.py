from abc import ABC, abstractmethod
from collections.abc import Callable, Hashable
from typing import Any, ClassVar, TypeVar, cast

import punq

__all__ = (
    "IoC",
    "GetStrategy",
    "GetResolverStrategy",
)

_T = TypeVar("_T")


class AbstractStrategy(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class GetStrategy(AbstractStrategy):
    def __call__(self, service_key: str, **kwargs: Any) -> Any:
        return cast(_T, IoC.container.resolve(service_key, **kwargs))


class GetResolverStrategy(AbstractStrategy):
    """Use in as DI

    SomeServiceT = Annotated[
        SomeService,
        Depends(
            IoC.resolve(SearchListService, strategy=GetResolverStrategy),
        ),
    ]
    """

    def __call__(self, service_key: type[_T], **kwargs: dict[Hashable, Any]) -> Callable[..., Any]:
        def resolve_type() -> _T:
            return cast(_T, IoC.container.resolve(service_key, **kwargs))

        return resolve_type


class IoC:
    container: ClassVar[punq.Container] = punq.Container()

    @staticmethod
    def strategy(service_key: str, **kwargs: Any) -> Any:
        return cast(_T, IoC.container.resolve(service_key, **kwargs))

    @staticmethod
    def resolve(service_key: str | type, strategy: AbstractStrategy = GetStrategy(), **kwargs: Any) -> Any:
        return strategy(service_key=service_key, **kwargs)
