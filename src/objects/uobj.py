from collections import UserDict
from typing import Any
from uuid import uuid4

__all__ = ("UObject",)


class UObject(UserDict):
    """Универсальный объект, отвечающий за параметры объекта. Фактически, немного расширенный dict."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.__hash: int = hash(str(uuid4()))

    def __hash__(self) -> int:
        return self.__hash

    def __eq__(self, other: object) -> bool:
        return self is other
