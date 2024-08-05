import logging
from threading import current_thread, get_ident

from commands.abstract_ import AbstractCommand

__all__ = ("SoftStopCommand",)

logger = logging.getLogger(__name__)


class SoftStopCommand(AbstractCommand):
    def execute(self) -> None:
        from conditions import SoftStopHandleCondition
        from container import StorageCondition

        logger.warning("Changing condition!, %s, %s", current_thread().name, get_ident())
        StorageCondition.condition_strategies[current_thread().name] = SoftStopHandleCondition
