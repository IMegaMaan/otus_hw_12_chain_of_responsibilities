from commands.abstract_ import AbstractCommand
from commands.check_object_intersection import CheckUObjectAreaCommand
from commands.injectable import InjectCommand
from commands.move_u_object import MoveCommand

__all__ = ("MoveMacroCommand",)

"""
1. определяет окрестность, в которой присутствует игровой объект
2. если объект попал в новую окрестность, то удаляет его из списка объектов старой окрестности и добавляет список 
объектов новой окрестности.
3. для каждого объекта новой окрестности и текущего движущегося объекта создает команду проверки коллизии этих двух 
объектов. Все эти команды помещает в макрокоманду и эту
макрокоманду записывает на место аналогичной макрокоманды для предыдущей окрестности.
"""


# TODO основная команда на движение.
class MoveMacroCommand(AbstractCommand):
    """Для каждого объекта новой окрестности и текущего движущегося объекта создает команду
    проверки коллизии этих двух объектов. Все эти команды помещает в макрокоманду и эту
    макрокоманду записывает на место аналогичной макрокоманды для предыдущей окрестности.

    """

    handlers: tuple[type[AbstractCommand]] = (
        MoveCommand,  # 1. двигаем объект
        CheckUObjectAreaCommand,  # 2. проверяет, изменил ли объект свою окрестность.
        # TODO тут еще надо будет добавить CheckCollisionCommand
        InjectCommand,
    )

    # # TODO требуется добавить???
    # def __init__(self, handlers) -> None: ...

    def execute(self) -> None:
        # TODO реализовать!!!!
        for cmd in MoveMacroCommand.handlers:
            cmd().execute()
