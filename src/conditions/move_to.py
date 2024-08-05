import logging
import threading
from queue import Queue

from conditions.base import BaseHandleCondition

__all__ = ("MoveToHandleCondition",)

logger = logging.getLogger(__name__)


class MoveToHandleCondition(BaseHandleCondition):
    thread_safe_storage = threading.local()

    def run_command_try(self) -> None:
        new_queue = getattr(MoveToHandleCondition.thread_safe_storage, "new_queue", None)
        if not new_queue:
            self.__create_queue()

        new_queue.put((self._command_class, self._kwargs))

    def __create_queue(self) -> None:
        from container import StorageCondition
        from main import Consumer

        logger.info("New thread command execute start!")

        new_queue = Queue()
        consumer = threading.Thread(target=Consumer.consume, args=(new_queue,))
        StorageCondition.queues[consumer.name] = new_queue
        StorageCondition.threads.append(consumer)
        MoveToHandleCondition.thread_safe_storage.new_queue = new_queue
