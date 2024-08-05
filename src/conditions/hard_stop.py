import logging

from conditions.base import BaseHandleCondition

__all__ = ("HardStopHandleCondition",)

logger = logging.getLogger(__name__)


class HardStopHandleCondition(BaseHandleCondition):
    def run_thread(self) -> bool:
        class_name = self.__class__.__name__
        logger.info(f"Condition was changed to {class_name}")

        return False
