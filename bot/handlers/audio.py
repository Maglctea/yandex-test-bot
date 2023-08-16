from aiogram import types

from bot.bot_texts import AUDIO_SELECTION
from bot.settings import MEDIA
from bot.structure.keyboards.audio_board import AUDIO_BOARD


async def audio(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        AUDIO_SELECTION,
        reply_markup=AUDIO_BOARD,
    )
    await callback.message.delete()


async def send_audio(callback: types.CallbackQuery, path: str = None) -> None:
    audio = types.FSInputFile(path)
    await callback.message.answer_voice(audio, reply_markup=AUDIO_BOARD)


async def send_gpt_audio(callback: types.CallbackQuery):
    path = str(MEDIA) + r'\GPT.mp3'
    await send_audio(callback, path)
    await callback.message.delete()

async def send_database_audio(callback: types.CallbackQuery):
    path = str(MEDIA) + r'\database.mp3'
    await send_audio(callback, path)
    await callback.message.delete()


async def send_love_story_audio(callback: types.CallbackQuery):
    path = str(MEDIA) + r'\love.mp3'
    await send_audio(callback, path)
    await callback.message.delete()
