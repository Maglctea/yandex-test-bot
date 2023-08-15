import enum

from aiogram.filters.callback_data import CallbackData


class PicturesMenuActions(enum.IntEnum):
    SELFIE = 1
    SCHOOL_PHOTO = 2
    BACK = 3


class PicturesMenuCallback(CallbackData, prefix="main_menu"):
    """
    Statistic callback
    """
    action: PicturesMenuActions


class MainMenuActions(enum.IntEnum):
    """
        Statistic actions
    """
    SEE_PICTURES = 1


class MainMenuCallback(CallbackData, prefix="statistic"):
    """
    Statistic callback
    """
    action: MainMenuActions
