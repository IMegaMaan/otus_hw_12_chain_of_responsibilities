__all__ = (
    "CollisionError",
    "CantStartThreadError",
    "ChangedAreaError",
)


class CollisionError(Exception): ...


class CantStartThreadError(Exception): ...


class ChangedAreaError(Exception): ...
