"""
Main
"""
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from bot.bot_texts import BOT_COMMANDS_INFO
from bot.handlers import *

from bot.settings import BOT_KEY, logger


async def async_main() -> None:
    # init bot
    storage = MemoryStorage()
    bot = Bot(token=BOT_KEY)
    dp = Dispatcher(storage=storage)

    # help commands
    commands_for_bot = []
    for cmd in BOT_COMMANDS_INFO:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    await bot.set_my_commands(commands_for_bot)

    # add handlers
    register_user_commands(dp)

    await dp.start_polling(bot)


def main():
    try:
        asyncio.run(async_main())
    except (KeyboardInterrupt, SystemExit):
        logger.debug("Bot stopped")


if __name__ == "__main__":
    main()
