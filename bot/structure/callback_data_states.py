import enum

from aiogram.filters.callback_data import CallbackData


class AudioMenuActions(enum.IntEnum):
    GPT = 1
    DATABASE = 2
    LOVE_STORY = 3
    BACK = 4


class AudioMenuCallback(CallbackData, prefix="audio_menu"):
    """
    Statistic callback
    """
    action: AudioMenuActions


class PicturesMenuActions(enum.IntEnum):
    SELFIE = 1
    SCHOOL_PHOTO = 2
    BACK = 3


class PicturesMenuCallback(CallbackData, prefix="pictures_menu"):
    """
    Statistic callback
    """
    action: PicturesMenuActions


class MainMenuActions(enum.IntEnum):
    """
        Statistic actions
    """
    SEE_PICTURES = 1
    SEE_AUDIO = 2

class MainMenuCallback(CallbackData, prefix="main_menu"):
    """
    Statistic callback
    """
    action: MainMenuActions
