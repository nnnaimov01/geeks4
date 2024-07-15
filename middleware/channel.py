from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot


CHANNELS = [{
    'channel_id': '-1002200988241',
    'username': 'geeks_group_4'
}]

class ChannelMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        user = message.from_user
        ibtn = InlineKeyboardMarkup()
        for channel in CHANNELS:
            user_channel = await bot.get_chat_member(user_id=int(user.id), chat_id=channel.get('channel_id'))
            print(user_channel)
            if user_channel.status == 'left':
                ibtn.add(
                    InlineKeyboardButton(text=channel.get('username'), url=f"https://t.me/{channel.get('username')}"),
                )
                await message.answer("Iltimos kanalga azo buling:", reply_markup=ibtn)
                raise CancelHandler()