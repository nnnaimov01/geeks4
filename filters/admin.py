from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from loader import ADMIN


class IsAdmin(BoundFilter):
    async def check(self, message: Message) -> bool:
        if message.from_user.id == int(ADMIN):
            return True
        else:
            return False

