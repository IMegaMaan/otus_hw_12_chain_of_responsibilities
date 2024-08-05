from commands.empty import EmptyCommand
from commands.injectable import InjectCommand


def test_empty_command_no_kwargs(empty_command: type[EmptyCommand]) -> None:
    cmd = empty_command({})
    cmd.execute()

    assert cmd._context == {}


def test_empty_command_with_kwargs(empty_command: type[EmptyCommand]) -> None:
    data_context = {
        "some_kwarg1": 1,
        "some_kwarg2": 2,
    }
    cmd = empty_command(data_context)
    cmd.execute()

    assert cmd._context == data_context


def test_injectable_command_default(inject_command: type[InjectCommand]) -> None:
    cmd = inject_command(context={})

    assert cmd._command is EmptyCommand


def test_injectable_command_inject_fixture_command(
    inject_command: type[InjectCommand],
    fixture_command: type["ExtraCommand"],  # noqa: F821
) -> None:
    data = {
        "command": fixture_command,
        "divisible": 4,
        "divider": 2,
    }
    cmd = inject_command(data)
    cmd.execute()

    assert cmd._context == {"result": 2}
