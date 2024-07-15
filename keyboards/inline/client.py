from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def social_ibtn():
    ibtn = InlineKeyboardMarkup()
    ibtn.add(InlineKeyboardButton("Google", callback_data="google"))
    ibtn.add(InlineKeyboardButton("Youtube", callback_data="youtube"))
    return ibtn


async def voice_ibtn():
    lbtn = InlineKeyboardMarkup()
    lbtn.add(InlineKeyboardButton("👍", callback_data="like"))
    lbtn.add(InlineKeyboardButton("👎", callback_data="dislike"))
    return lbtn