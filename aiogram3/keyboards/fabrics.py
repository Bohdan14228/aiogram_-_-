from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(CallbackData, prefix='pag'):
    action: str
    page: int

def pagination(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🔙", callback_data=Pagination(action='prev', page=page).pack()),
        InlineKeyboardButton(text="🔜", callback_data=Pagination(action='next', page=page).pack()),
        width=2     # означает что два кнопки будут вряд
    )
    return builder.as_markup()