from adapters import IGetArea, IMovableForward
from commands.abstract_ import AbstractCommand
from commands.check_object_intersection import CheckUObjectAreaCommand
from commands.exceptions import ChangedAreaError
from commands.injectable import InjectCommand
from commands.macro_check_collision import CheckCollisionMacroCommand
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


class MoveMacroCommand(AbstractCommand):
    """Для каждого объекта новой окрестности и текущего движущегося объекта создает команду
    проверки коллизии этих двух объектов. Все эти команды помещает в макрокоманду и эту
    макрокоманду записывает на место аналогичной макрокоманды для предыдущей окрестности.
    """

    def execute(self) -> None:
        MoveCommand(self._context, IMovableForward()).execute()
        try:
            CheckUObjectAreaCommand(self._context, IGetArea(), IMovableForward()).execute()
        except ChangedAreaError:
            self._context.update(
                {"command": CheckCollisionMacroCommand},
            )
        # тут происходит выполнение нужной команды в случае выполнения ексепшена.
        #  Фактически, можно в дальнейшем перенести и в handlers ошибок.
        InjectCommand(self._context).execute()
