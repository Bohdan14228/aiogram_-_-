from aiogram.types import *

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/watch?v=CBJiJcgmDmM&t=376s'),
            InlineKeyboardButton(text='YouTube2', url='tg://resolve?domain=mr_lazba'),
            InlineKeyboardButton(text='lazbs', url='tg://resolve?domain=mr_lazba'),
        ]
    ]
)