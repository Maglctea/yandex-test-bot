__all__ = [
    "register_user_commands",
]

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.handlers.help import help_command, help_func
from bot.handlers.pictures import pictures, send_selfie, send_school_photo
from bot.handlers.start import start, start_callback
from bot.structure.callback_data_states import PicturesMenuCallback, MainMenuActions, PicturesMenuActions, \
    MainMenuCallback


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

    # pictures
    router.callback_query.register(pictures, MainMenuCallback.filter(
        F.action == MainMenuActions.SEE_PICTURES
    ))
    router.callback_query.register(send_selfie, PicturesMenuCallback.filter(
        F.action == PicturesMenuActions.SELFIE
    ))
    router.callback_query.register(send_school_photo, PicturesMenuCallback.filter(
        F.action == PicturesMenuActions.SCHOOL_PHOTO
    ))
    router.callback_query.register(start_callback, PicturesMenuCallback.filter(
        F.action == PicturesMenuActions.BACK
    ))

