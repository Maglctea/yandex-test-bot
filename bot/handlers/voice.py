from aiogram import types

from bot.bot_texts import VOICE_COMMANDS
from bot.settings import MEDIA
from bot.utils.voice import ogg2text


async def voice_handler(message: types.Message) -> None:
    file_id = message.voice.file_id
    bot = message.voice.get_mounted_bot()
    file_url = (await bot.get_file(file_id)).file_path
    bytes_ = await bot.download_file(file_url)

    path = fr'{str(MEDIA)}\upload\{file_id}.ogg'

    with open(path, 'wb') as f:
        f.write(bytes_.read())

    text = ogg2text(path)
    answer = VOICE_COMMANDS.get(text.lower())
    await message.answer(answer if answer else 'Команда не распознана!')
