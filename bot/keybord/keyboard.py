from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('валюта')
b2 = KeyboardButton('акции')
b3 = KeyboardButton('крипта')
kb=ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(b1).add(b2).add(b3)


a1 = KeyboardButton('Доллар')
a2 = KeyboardButton('Евро')
a3 = KeyboardButton('Юань')
ka=ReplyKeyboardMarkup(resize_keyboard=True)
ka.add(a1).add(a2).add(a3)

c1 = KeyboardButton('Сбербанк')
c2 = KeyboardButton('Газпром')
c3 = KeyboardButton('Норникель')
kc=ReplyKeyboardMarkup(resize_keyboard=True)
kc.add(c1).add(c2).add(c3)

d1 = KeyboardButton('Биткоин')
d2 = KeyboardButton('Эфир')
kd=ReplyKeyboardMarkup(resize_keyboard=True)
kd.add(d1).add(d2)