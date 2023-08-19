__all__ = [
    "register_user_commands",
]

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from bot.handlers.audio import audio_select_file, audio_callback_answer
from bot.handlers.help import help_command, help_func, blog_command, links_command
from bot.handlers.pictures import picture_select_file, picture_callback_answer
from bot.handlers.start import start
from bot.handlers.voice import voice_handler
from bot.structure import (
    PicturesMenuCallback,
    MainMenuActions,
    MainMenuCallback,
    AudioMenuCallback
)


def register_user_commands(router: Router) -> None:
    """
    Register user commands
    :param router:
    :return:
    """
    # start
    router.message.register(voice_handler, F.voice)
    router.message.register(start, CommandStart())

    # help
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(help_func, F.text.capitalize() == "Помощь")

    # links
    router.message.register(links_command, Command(commands=["links"]))
    # blog
    router.message.register(blog_command, Command(commands=["blog"]))

    # pictures
    router.callback_query.register(picture_select_file, MainMenuCallback.filter(
        F.action == MainMenuActions.SEE_PICTURES
    ))
    router.callback_query.register(picture_callback_answer, PicturesMenuCallback.filter())

    # audio
    router.callback_query.register(audio_select_file, MainMenuCallback.filter(
        F.action == MainMenuActions.SEE_AUDIO
    ))
    router.callback_query.register(audio_callback_answer, AudioMenuCallback.filter())


