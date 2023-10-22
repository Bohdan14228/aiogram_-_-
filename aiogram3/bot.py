import asyncio
import logging
import sys
from os import getenv
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram3.callbacks import pagination
from aiogram3.handlers import bot_messages, user_commands, questionaire
from config_reader import config


# @dp.message(F.text == '/play')
# async def play(message: Message):
#     x = await message.answer_dice(DiceEmoji.DICE)
#     print(x.dice.value)


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionaire.router,
        bot_messages.router
    )
    bot = Bot(config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())