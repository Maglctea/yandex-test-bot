import enum

from aiogram.filters.callback_data import CallbackData


class AudioMenuActions(enum.IntEnum):
    """
    Audio menu actions
    """
    GPT = 1
    DATABASE = 2
    LOVE_STORY = 3
    BACK = 4


class AudioMenuCallback(CallbackData, prefix="audio_menu"):
    """
    Audio callback
    """
    action: AudioMenuActions


class PicturesMenuActions(enum.IntEnum):
    """
    Pictures menu actions
    """
    SELFIE = 1
    SCHOOL_PHOTO = 2
    BACK = 3


class PicturesMenuCallback(CallbackData, prefix="pictures_menu"):
    """
    Pictures menu callback
    """
    action: PicturesMenuActions


class MainMenuActions(enum.IntEnum):
    """
    Main menu actions
    """
    SEE_PICTURES = 1
    SEE_AUDIO = 2


class MainMenuCallback(CallbackData, prefix="main_menu"):
    """
    Main menu callback
    """
    action: MainMenuActions
