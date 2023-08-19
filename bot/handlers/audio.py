from aiogram import types

from bot.bot_texts import AUDIO_SELECTION
from bot.handlers.start import start
from bot.settings import MEDIA
from bot.structure import AudioMenuActions, AudioMenuCallback
from bot.structure.keyboards import AUDIO_BOARD


async def audio_select_file(
        callback: types.CallbackQuery,
) -> None:
    await callback.message.answer(
        AUDIO_SELECTION,
        reply_markup=AUDIO_BOARD,
    )
    await callback.message.delete()


async def audio_callback_answer(
        callback: types.CallbackQuery,
        callback_data: AudioMenuCallback
) -> None:
    path = None
    match callback_data.action:
        case AudioMenuActions.GPT:
            path = str(MEDIA) + '/GPT.mp3'
        case AudioMenuActions.DATABASE:
            path = str(MEDIA) + '/database.mp3'
        case AudioMenuActions.LOVE_STORY:
            path = str(MEDIA) + '/love.mp3'
        case AudioMenuActions.BACK:
            return await start(callback.message)
    if path:
        audio_ = types.FSInputFile(path)
        await callback.message.answer_voice(audio_, reply_markup=AUDIO_BOARD)
        await callback.message.delete()

