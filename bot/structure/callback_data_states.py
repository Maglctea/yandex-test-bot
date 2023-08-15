import enum

from aiogram.filters.callback_data import CallbackData


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
