import logging
import sys
from queue import Queue
from threading import Thread, current_thread, get_ident

from commands import MoveMacroCommand
from commands.hard_stop import HardStopCommand
from commands.soft_stop import SoftStopCommand
from commands.start_consumer_in_thread import StartConsumerInThreadCommand
from conditions.abstract_ import AbstractHandleCondition
from constants import BASE_DIR, LOGGING_FORMAT, LOGGING_LEVEL
from container import StorageCondition
from ioc import register_commands

__all__ = (
    "Consumer",
    "Producer",
)

logger = logging.getLogger(__name__)


class Consumer:
    def __init__(self) -> None:
        register_commands()
        self._prepare_logging()

    def _prepare_logging(self) -> None:
        logging.basicConfig(
            level=LOGGING_LEVEL,
            format=LOGGING_FORMAT,
            handlers=[
                logging.FileHandler(BASE_DIR / "output.log"),
                logging.StreamHandler(sys.stdout),
            ],
        )

    def init_consumer(self) -> Thread:
        """Initialize consumer."""
        new_queue = Queue()
        thread = Thread(target=self.consume, args=(new_queue,))
        StorageCondition.queues[thread.name] = new_queue
        StorageCondition.threads.append(thread)
        StorageCondition.threads.append(thread)

        return thread

    @staticmethod
    def run_consumer(thread: Thread) -> None:
        thread.start()

    @staticmethod
    def run_all_consumers() -> None:
        """Run all consumers."""
        for thread in StorageCondition.threads:
            thread.start()

    @staticmethod
    def consume(queue: Queue) -> None:
        """Mains command to start consume."""
        thread_id: int = get_ident()
        thread_name: str = current_thread().name
        condition = StorageCondition.default_condition(queue, thread_id)
        while condition.run_thread():
            condition.handle()
            condition_class: type[AbstractHandleCondition] = Consumer._get_condition_or_default(thread_name)
            condition = condition_class(queue, thread_id)
        logger.info(f"The end of thread {thread_id}")
        del StorageCondition.queues[thread_name]  # clear queue of concrete thread

    @staticmethod
    def _get_condition_or_default(thread_name: str) -> type[AbstractHandleCondition]:
        return StorageCondition.condition_strategies.get(thread_name, StorageCondition.default_condition)


class Producer:
    def __init__(self) -> None:
        register_commands()

    @staticmethod
    def put_command_start(queue: Queue) -> None:
        extra_data = {}
        queue.put((StartConsumerInThreadCommand, extra_data))

    @staticmethod
    def put_command_hard_stop(queue: Queue) -> None:
        extra_data = {}
        queue.put((HardStopCommand, extra_data))

    @staticmethod
    def put_command_move_to(queue: Queue) -> None:
        extra_data = {}
        queue.put((MoveMacroCommand, extra_data))  # TODO положить сюда движение макро команду

    @staticmethod
    def put_command_soft_stop(queue: Queue) -> None:
        extra_data = {}
        queue.put((SoftStopCommand, extra_data))


def init_main_consumer() -> Consumer:
    return Consumer()


def init_in_thread_consumer(main_consumer: Consumer) -> Thread:
    return main_consumer.init_consumer()


def init_task_hard_stop(queue: Queue) -> None:
    Producer.put_command_hard_stop(queue=queue)
    Producer.put_command_start(queue=queue)


def init_task_soft_stop(queue: Queue) -> None:
    Producer.put_command_soft_stop(queue=queue)
    Producer.put_command_start(queue=queue)


if __name__ == "__main__":
    main_consumer = init_main_consumer()
    in_thread_consumer = init_in_thread_consumer(main_consumer)
    queue = StorageCondition.queues[in_thread_consumer.name]

    init_task_hard_stop(queue)
    # init_task_soft_stop(queue)
    # init_task_soft_stop(queue)

    main_consumer.run_consumer(in_thread_consumer)
