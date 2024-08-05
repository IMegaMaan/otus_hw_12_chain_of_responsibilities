from adapters.intersection import IGetArea
from commands.abstract_ import AbstractCommand
from objects import Context

__all__ = ("CheckUObjectAreaCommand",)


class CheckUObjectAreaCommand(AbstractCommand):
    """- Определяет окрестность, в которой присутствует игровой объект.
        - Реализация сейчас не требуется. Будем считать, что заложена некотороая логика.
    - если объект попал в новую окрестность, то удаляет его из списка объектов старой окрестности и добавляет
    список объектов новой окрестности.


    - для каждого объекта новой окрестности и текущего движущегося объекта создает команду проверки коллизии этих двух
    объектов. Все эти команды помещает в макрокоманду и эту
    макрокоманду записывает на место аналогичной макрокоманды для предыдущей окрестности.
    """

    def __init__(self, context: Context, i_intersection: IGetArea) -> None:
        super().__init__(context)
        self.__i_intersection = i_intersection

    def execute(self) -> None: ...
