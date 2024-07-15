from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from loader import dp, bot, ADMIN
from aiogram import types
from keyboards.inline import voice_ibtn
from keyboards.default import start_btn, start_btn_admin
from utils.database import users
from states import MyStates
import requests


HELP_TEXT = f"""
<b>/start</b> - <em>botni ishga tushirish</em>
/help - yordam berish
"""

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id == int(ADMIN):
        await message.answer("Assalom aleykum ADMIN!!!", reply_markup=await start_btn_admin())
    else:
        user = users.get_users(user_id)
        if not user:
            users.create_user(user_id, message.from_user.full_name)
        await message.answer("Assalom aleykum botimizga xush kelibsiz", reply_markup=await start_btn())
        await message.answer("ismizni kiriting:")
        await MyStates.request_name.set()


@dp.message_handler(state=MyStates.request_name)
async def request_name(message: types.Message):
    user_id = message.from_user.id
    name = message.text
    print("name - ", name)
    await message.answer("Yoshizni kiritng:")
    await MyStates.request_age.set()

@dp.message_handler(state=MyStates.request_age)
async def request_name(message: types.Message):
    user_id = message.from_user.id
    age = message.text
    print("age -", age)
    await message.answer("telefon nomerizni kiritng:")
    await MyStates.request_phone.set()


@dp.message_handler(state=MyStates.request_phone)
async def request_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    phone = message.text
    print("phone -", phone)
    await state.finish()



@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
    data = call.data
    await call.answer(data)
    # await call.message.answer(data)

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(HELP_TEXT, parse_mode="HTML", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=["photo"])
async def photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://ingredienta.com/wp-content/uploads/2023/03/0LIMONORGANICO.png", caption="yoqdimi sizga??")


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact(message: types.Message):
    phone = message.contact.phone_number
    user_id = message.contact.user_id
    users.update_user(user_id, phone)
    await message.answer("Qabul qilindi!")

@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def lokasiya(message: types.Message):
    user_id = message.from_user.id
    longitude = message.location.longitude
    latitude = message.location.latitude
    users.update_user_location(user_id, longitude, latitude)
    await message.answer("Qabul qilindi!")



@dp.message_handler(commands=["sticker"])
async def sticker(message: types.Message):
    print("send stiker")
    await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEMWXdmdZ-RbXQ_acZGmfHrhx2JBeQ5XQACfwADwZxgDNbKlU5SM1p7NQQ")

@dp.message_handler(commands=["voice"])
async def voice(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://ingredienta.com/wp-content/uploads/2023/03/0LIMONORGANICO.png", caption="yoqdimi sizga??", reply_markup=await voice_ibtn())


@dp.message_handler(commands=["currency"])
async def currency(message: types.Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    data = response.json()
    for item in data:
        if item['Ccy'] == "USD" or item['Ccy'] == "EUR" or item['Ccy'] == "RUB":
            valyuta = item['Ccy']
            nomi = item['CcyNm_UZ']
            rate = item['Rate']
            date = item['Date']

            text = (f"<b>{nomi}</b>\n"
                    f"<b>1{valyuta}</b> - {rate} so'm\n"
                    f"<b>Sana</b> - {date}")
            await message.answer(text, parse_mode="HTML")


@dp.message_handler(commands=["weather"])
async def weather(message: types.Message):
    response = requests.get("https://api.weatherapi.com/v1/current.json?key=637a0367057542d9936143247240705&q=Tashkent")
    data = response.json()
    text = (f"<b>{data['location']['name']}</b>\n"
            f"<b>Vaqt mintaqasi</b> - {data['location']['tz_id']}\n"
            f"<b>Sana</b> - {data['location']['localtime']}\n"
            f"<b>Xarorat</b> - {data['current']['temp_c']}°C\n"
            f"Shamol - {data['current']['wind_mph']}m/s\n")
    await message.answer(text, parse_mode="HTML")





@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(chat_id=message.chat.id, text=message.text)
