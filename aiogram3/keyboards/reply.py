from aiogram.types import *

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='смайлики'),
            KeyboardButton(text='ссылки')
        ],
        [
            KeyboardButton(text='калькулятор'),
            KeyboardButton(text='спец. кнопки')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Enter text',
    selective=True
)

spec_ikb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить гео', request_location=True),
            KeyboardButton(text='Отправить контакт', request_contact=True),
            KeyboardButton(text='Отправить гео', request_poll=KeyboardButtonPollType())  # quiz викторина, regular голосование
        ],
        [
            KeyboardButton(text='<-')
        ]

    ],
    resize_keyboard=True
)

rmk = ReplyKeyboardRemove()