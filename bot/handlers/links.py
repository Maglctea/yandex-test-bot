from aiogram import types
from aiogram.filters import CommandObject

from bot.bot_texts import LINKS_TEXT


async def links_command(message: types.Message, command: CommandObject):
    """
    help command detail
    :param message:
    :param command:
    :return SendMessage:
    """
    return await message.answer(LINKS_TEXT)
