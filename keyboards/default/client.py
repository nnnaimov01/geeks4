from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton("/start")).insert(KeyboardButton("/help"))
    btn.add(KeyboardButton("/photo")).insert(KeyboardButton("/sticker"))
    btn.add(KeyboardButton("Контакт", request_contact=True)).insert(KeyboardButton("Lokasiya", request_location=True))
    return btn

