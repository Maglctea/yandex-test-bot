__all__ = [
    "register_user_commands",
]

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.handlers.audio import audio, send_gpt_audio, send_database_audio, send_love_story_audio
from bot.handlers.blog import blog_command
from bot.handlers.help import help_command, help_func
from bot.handlers.links import links_command
from bot.handlers.pictures import pictures, send_selfie, send_school_photo
from bot.handlers.start import start, start_callback
from bot.structure.callback_data_states import PicturesMenuCallback, MainMenuActions, PicturesMenuActions, \
    MainMenuCallback, AudioMenuActions, AudioMenuCallback


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

    # links
    router.message.register(links_command, Command(commands=["links"]))

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

    # blog
    router.message.register(blog_command, Command(commands=["blog"]))

    # audio
    router.callback_query.register(audio, MainMenuCallback.filter(
        F.action == MainMenuActions.SEE_AUDIO
    ))
    router.callback_query.register(send_gpt_audio, AudioMenuCallback.filter(
        F.action == AudioMenuActions.GPT
    ))
    router.callback_query.register(send_database_audio, AudioMenuCallback.filter(
        F.action == AudioMenuActions.DATABASE
    ))
    router.callback_query.register(send_love_story_audio, AudioMenuCallback.filter(
        F.action == AudioMenuActions.LOVE_STORY
    ))
    router.callback_query.register(start_callback, AudioMenuCallback.filter(
        F.action == AudioMenuActions.BACK
    ))
