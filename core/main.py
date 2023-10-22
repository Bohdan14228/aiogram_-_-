import asyncio
import sys
from aiogram import Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
import logging
from core.handlers.basic import *
from core.settings import setting


async def start_bot(bot: Bot):
    await bot.send_message(setting.bots.admin_id, 'Бот запущен!')

async def stop_bot(bot: Bot):
    await bot.send_message(setting.bots.admin_id, 'Бот остановлен!')

async def main() -> None:
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(token=setting.bots.bot_token, parse_mode=ParseMode.HTML)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(start, CommandStart())
    dp.message.register(get_photo)
    dp.message.register(get_audio)

    # await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())