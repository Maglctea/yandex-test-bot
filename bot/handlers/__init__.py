__all__ = [
    "register_user_commands",
]

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.handlers.help import help_command, help_func
from bot.handlers.start import start


def register_user_commands(router: Router) -> None:
    """
    Register user commands
    :param router:
    :return:
    """
    # start
    router.message.register(start, CommandStart())

    # help
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(help_func, F.text.capitalize() == "Помощь")

