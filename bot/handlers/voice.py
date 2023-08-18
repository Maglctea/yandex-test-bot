from aiogram import types
from datetime import datetime
from bot.settings import MEDIA
from bot.utils.voice import ogg2text


async def audio(message: types.Message) -> None:
    if message.content_type == types.ContentType.VOICE:
        file_id = message.voice.file_id
        bot = message.voice.get_mounted_bot()
        file = await bot.get_file(file_id)
        file_url = file.file_path
        bytes = await bot.download_file(file_url)

        filename = f'{file_id}.ogg'
        path = fr'{str(MEDIA)}\upload\{filename}'
        with open(path, 'wb') as f:
            f.write(bytes.read())

        text = ogg2text(path)

        match text:
            case 'Время':
                await message.answer(f'Сейчас {datetime.now()}')
            case 'Привет':
                await message.answer('Приввет! Я тестовый бот')
            case _:
                await message.answer('Команда не распознана!')
