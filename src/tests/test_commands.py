from unittest.mock import Mock

from commands import CheckUObjectAreaCommand, EmptyCommand, InjectCommand, MoveMacroCommand
from objects import Context, UObject


def test_empty_command_no_kwargs(empty_command: type[EmptyCommand]) -> None:
    cmd = empty_command(Context())
    cmd.execute()

    assert cmd._context == {}


def test_empty_command_with_kwargs(empty_command: type[EmptyCommand]) -> None:
    data_context = Context(
        {
            "some_kwarg1": 1,
            "some_kwarg2": 2,
        },
    )
    cmd = empty_command(data_context)
    cmd.execute()

    assert cmd._context == data_context


def test_injectable_command_default(inject_command: type[InjectCommand]) -> None:
    cmd = inject_command(Context())

    assert cmd._command is EmptyCommand


def test_injectable_command_inject_fixture_command(
    inject_command: type[InjectCommand],
    fixture_command: type["ExtraCommand"],  # noqa: F821
) -> None:
    context_data = Context(
        {
            "command": fixture_command,
            "divisible": 4,
            "divider": 2,
        },
    )
    cmd = inject_command(context_data)
    cmd.execute()

    assert cmd._context == Context({"result": 2})


def test_macro_move_no_need_change_location(macro_move: type[MoveMacroCommand], u_object: UObject) -> None:
    context_data = Context({"u_object": u_object})
    cmd = macro_move(context_data)

    cmd.execute()


def test_macro_move_need_to_change_location(macro_move: type[MoveMacroCommand], u_object: UObject, mocker) -> None:
    mocker.patch("commands.CheckUObjectAreaCommand.execute", Mock(side_effect=CheckUObjectAreaCommand.raise_error))
    mocker.patch("commands.CheckLocationCommand.execute")

    context_data = Context({"u_object": u_object})
    cmd = macro_move(context_data)

    cmd.execute()
