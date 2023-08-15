from aiogram import types
from aiogram.types import InputFile

from bot.bot_texts import PICTURE_SELECTION, SCHOOL_PHOTO_DESCRIPTION
from bot.settings import MEDIA
from bot.structure.keyboards.picture_board import PICTURES_BOARD


async def pictures(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        PICTURE_SELECTION,
        reply_markup=PICTURES_BOARD,
    )
    await callback.message.delete()


async def send_photo(callback: types.CallbackQuery, path: str, caption: str = None) -> None:
    image = types.FSInputFile(path)
    await callback.message.answer_photo(image, caption, reply_markup=PICTURES_BOARD)


async def send_selfie(callback: types.CallbackQuery) -> None:
    path = str(MEDIA) + r'\selfie.jpg'
    await send_photo(callback, path)
    await callback.message.delete()


async def send_school_photo(callback: types.CallbackQuery) -> None:
    path = str(MEDIA) + r'\school.jpg'
    await send_photo(callback, path, SCHOOL_PHOTO_DESCRIPTION)
    await callback.message.delete()
