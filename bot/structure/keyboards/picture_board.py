from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.structure.callback_data_states import PicturesMenuActions, PicturesMenuCallback

builder = InlineKeyboardBuilder()

builder.button(
    text="Селфи", callback_data=PicturesMenuCallback(action=PicturesMenuActions.SELFIE)
)
builder.button(
    text="Школьное фото", callback_data=PicturesMenuCallback(action=PicturesMenuActions.SCHOOL_PHOTO)
)
builder.button(
    text="Назад", callback_data=PicturesMenuCallback(action=PicturesMenuActions.BACK)
)

builder.adjust(1)

PICTURES_BOARD = builder.as_markup()




