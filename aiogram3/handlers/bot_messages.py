from aiogram.types import *
from aiogram import Router
from aiogram3.keyboards.reply import *
from aiogram3.keyboards.inline import *
from aiogram3.keyboards.fabrics import *
from aiogram3.keyboards.builders import *
from aiogram3.data.subloader import get_json

router = Router()

@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    smiles = await get_json('smiles.json')
    if msg == 'ссылки':
        await message.answer('Вот ваши ссылки', reply_markup=links_kb)
    elif msg == 'спец. кнопки':
        await message.answer('спец. кнопки', reply_markup=spec_ikb)
    elif msg == 'калькулятор':
        await message.answer('калькулятор', reply_markup=calc_kb())
    elif msg == 'смайлики':
        await message.answer(f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=pagination())
    elif msg == 'назад':
        await message.answer('Вы перешли в главное меню', reply_markup=main_kb)