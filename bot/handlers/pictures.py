from aiogram import types

from bot.bot_texts import PICTURE_SELECTION, SCHOOL_PHOTO_DESCRIPTION
from bot.handlers.start import start
from bot.settings import MEDIA, logger
from bot.structure import PicturesMenuCallback, PicturesMenuActions
from bot.structure.keyboards import PICTURES_BOARD


async def picture_select_file(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        PICTURE_SELECTION,
        reply_markup=PICTURES_BOARD,
    )
    await callback.message.delete()


async def picture_callback_answer(
        callback: types.CallbackQuery,
        callback_data: PicturesMenuCallback,
) -> None:
    path = None
    caption = None
    match callback_data.action:
        case PicturesMenuActions.SELFIE:
            path = str(MEDIA) + r'/selfie.jpg'
        case PicturesMenuActions.SCHOOL_PHOTO:
            path = str(MEDIA) + r'/school.jpg'
            caption = SCHOOL_PHOTO_DESCRIPTION
        case PicturesMenuActions.BACK:
            return await start(callback.message)

    image = types.FSInputFile(path)
    logger.error(path)
    await callback.message.answer_photo(image, caption, reply_markup=PICTURES_BOARD)
    await callback.message.delete()

