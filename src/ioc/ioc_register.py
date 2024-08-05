from commands import GetIoCCommand, GetResolverIocCommand, RegisterIoCCommand
from ioc.ioc_storage import IoC

__all__ = ("register_commands",)


def register_commands() -> None:
    # RegisterIoC
    IoC.container.register("RegisterIoCCommand", factory=RegisterIoCCommand)
    # GetIoCCommand
    IoC.resolve(
        "RegisterIoCCommand",
        context={
            "register_service_key": "GetIoCCommand",
            "factory": GetIoCCommand,
        },
    ).execute()
    # GetResolverIocCommand
    IoC.resolve(
        "RegisterIoCCommand",
        context={
            "register_service_key": "GetResolverIocCommand",
            "factory": GetResolverIocCommand,
        },
    ).execute()
