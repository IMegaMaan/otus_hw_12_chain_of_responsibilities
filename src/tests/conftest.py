import pytest

from commands.empty import EmptyCommand
from commands.injectable import InjectCommand
from objects import BattleField, UObject


@pytest.fixture()
def battle_field_4_4() -> BattleField:
    return BattleField(x=4, y=4)


@pytest.fixture()
def u_object() -> UObject:
    return UObject()


@pytest.fixture()
def empty_command() -> type[EmptyCommand]:
    return EmptyCommand


@pytest.fixture()
def inject_command() -> type[InjectCommand]:
    return InjectCommand


@pytest.fixture()
def fixture_command() -> type["ExtraCommand"]:
    from commands.abstract_ import AbstractCommand

    class ExtraCommand(AbstractCommand):
        def execute(self) -> None:
            divisible = self._context.pop("divisible")
            divider = self._context.pop("divider")
            result = divisible // divider
            self._context.update({"result": result})

    return ExtraCommand
