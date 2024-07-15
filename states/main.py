from aiogram.dispatcher.filters.state import State, StatesGroup


class MyStates(StatesGroup):
    request_name = State()
    request_phone = State()
    request_age = State()

class MyAdminStates(StatesGroup):
    request_message = State()
