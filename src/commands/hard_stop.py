import logging
from threading import current_thread, get_ident

from commands.abstract_ import AbstractCommand

__all__ = ("HardStopCommand",)

logger = logging.getLogger(__name__)


class HardStopCommand(AbstractCommand):
    def execute(self) -> None:
        from conditions import HardStopHandleCondition
        from container import StorageCondition

        logger.warning("Changing condition to HardStopHandleCondition!, %s, %s", current_thread().name, get_ident())
        StorageCondition.condition_strategies[current_thread().name] = HardStopHandleCondition
