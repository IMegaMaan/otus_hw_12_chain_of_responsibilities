import logging
from queue import Queue
from threading import Thread

from commands.abstract_ import AbstractCommand
from commands.exceptions import CantStartThreadError

__all__ = ("StartConsumerInThreadCommand",)

logger = logging.getLogger(__name__)


class StartConsumerInThreadCommand(AbstractCommand):
    raise_error = CantStartThreadError

    def execute(self) -> None:
        from container import StorageCondition
        from main import Consumer

        logger.info("New thread command execute start!")

        new_queue = Queue()
        consumer = Thread(target=Consumer.consume, args=(new_queue,))
        StorageCondition.queues[consumer.name] = new_queue
        StorageCondition.threads.append(consumer)

        consumer.start()
        logger.info("New thread command executed!")
