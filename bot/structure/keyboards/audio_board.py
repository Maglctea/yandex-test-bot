from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.structure.callback_data_states import AudioMenuCallback, AudioMenuActions

builder = InlineKeyboardBuilder()

builder.button(
    text="GPT", callback_data=AudioMenuCallback(action=AudioMenuActions.GPT)
)
builder.button(
    text="SQL и NoSQL", callback_data=AudioMenuCallback(action=AudioMenuActions.DATABASE)
)
builder.button(
    text="Любовные истории", callback_data=AudioMenuCallback(action=AudioMenuActions.LOVE_STORY)
)
builder.button(
    text="Назад", callback_data=AudioMenuCallback(action=AudioMenuActions.BACK)
)

builder.adjust(1)

AUDIO_BOARD = builder.as_markup()




