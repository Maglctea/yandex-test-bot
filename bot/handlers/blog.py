from aiogram.filters import CommandObject
from aiogram import types

from bot.bot_texts import TEXT_BLOG


async def blog_command(message: types.Message, command: CommandObject):
    """
    help command detail
    :param message:
    :param command:
    :return SendMessage:
    """
    return await message.answer(TEXT_BLOG)
