import random

from aiogram import types
from aiogram import Router
from aiogram.filters import *
from aiogram3.keyboards.reply import *

router = Router()

@router.message(CommandStart())
async def start(message: types.Message, command: CommandObject):
    # await message.answer(f"Hello <code>{message.from_user.first_name}</code>")
    # await message.answer(command.args)
    await message.answer('asasa', reply_markup=main_kb)

@router.message(Command(commands=['rn', 'random-number']))
async def get_random_number(message: types.Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split('-')]
    rnum = random.randint(a, b)

    await message.reply(f"Random number: {rnum}")