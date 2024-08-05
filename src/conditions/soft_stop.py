import logging

from conditions import BaseHandleCondition

__all__ = ("SoftStopHandleCondition",)

logger = logging.getLogger(__name__)


class SoftStopHandleCondition(BaseHandleCondition):
    def run_thread(self) -> bool:
        return not self._queue.empty()
