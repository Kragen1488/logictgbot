from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keybord import kb
from config import TOKEN
from keybord import ka
from keybord import kc
from keybord import kd

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Введи команду хелп для ознакомления")

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("Этот бот поможет тебе следить за валютой(/валюта),рынком ценных бумаг(/акции), и криптовалютой(/крипта) в скобках указаны команды для более подробного ознакомления",reply_markup=kb)

@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text == "валюта":
        await msg.reply("Наш бот предоставляет доступ к курсу: Доллару,Евро,Юаню относительно рубля",reply_markup=ka)
    elif msg.text == "акции":
        await msg.reply("Наш бот предоставляет доступ к стоимости акций: Сбербанк, Газпром, Норникель",reply_markup=kc)
    else:
        await msg.reply("Наш бот предоставляет доступ к курсу: Биткоина и Эфира относительно доллара",reply_markup=kd)


if __name__ == '__main__':
    executor.start_polling(dp)