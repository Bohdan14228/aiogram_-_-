import asyncio
import logging
import sys
from os import getenv
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import random

# TOKEN = getenv("6485142666:AAENzB1hFi3U144h9G1rowVRnIR26r7fRYA")
TOKEN = "6485142666:AAENzB1hFi3U144h9G1rowVRnIR26r7fRYA"
dp = Dispatcher()


@dp.message(Command(commands=['start', 'ps']))
async def start(message: types.Message, command: CommandObject):
    # await message.answer(f"Hello <code>{message.from_user.first_name}</code>")
    await message.answer(command.args)


@dp.message(F.text == '/play')
async def play(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    print(x.dice.value)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())