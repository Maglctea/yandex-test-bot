"""
start handler
"""
from aiogram import types

from bot.bot_texts import GREETING_TEXT
from bot.structure.keyboards import MAIN_BOARD


async def start(message: types.Message) -> None:

    await message.answer(
        GREETING_TEXT,
        reply_markup=MAIN_BOARD,
    )
    await message.delete()


async def start_callback(callback: types.CallbackQuery) -> None:

    await callback.message.answer(
        GREETING_TEXT,
        reply_markup=MAIN_BOARD,
    )
    await callback.message.delete()