from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.structure.callback_data_states import MainMenuCallback, MainMenuActions


builder = InlineKeyboardBuilder()

builder.button(
    text="Посмотреть", callback_data=MainMenuCallback(action=MainMenuActions.SEE_PICTURES)
)
builder.button(
    text="Аудио", callback_data=MainMenuCallback(action=MainMenuActions.SEE_AUDIO)
)

builder.button(
    text="Репозиторий”", url="https://github.com/Maglctea/yandex-test-bot"
)
builder.adjust(1)

MAIN_BOARD = builder.as_markup()




