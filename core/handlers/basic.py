from aiogram import types
from aiogram import Bot

async def start(message: types.Message, bot: Bot):
    await message.answer('<s>зачеркнутое</s>')
    await message.answer('<tg-spoiler>зачеркнутое</tg-spoiler>')

async def get_photo(message: types.Message, bot: Bot):
    await message.answer('Ты отправил картинку, я сохранил её себе')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_audio(message: types.Message, bot: Bot):
    await bot.send_audio(message.audio.title)