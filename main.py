import telebot # Импортируем telebot
import telegram
import random
from telebot import types # для определения типов
from secrets import secrets # импортируем словарь с токеном из файла secrets.py

# передаём значение переменной с кодом экземпляру бота
token = ('7062105451:AAEzx21-UAkOEqBDwMuxq9y9eb5LHL-YqTo')
bot = telebot.TeleBot(token)

# хендлер и функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здорова, отец")

# отправка фото Лены
@bot.message_handler(commands=['elenka', 'Elenka', 'lena_lopa', 'lena'])
def name_message(message):
    rand = random.randint(0,6)
    photo_path = './photos/elenka' + str(rand) + '.jpg'
    bot.send_photo(message.chat.id, open(photo_path, 'rb'))

# отправка фото Эдика
@bot.message_handler(commands=['edik', 'Edik', 'ed', 'Ed', 'vash_ed'])
def name_message(message):
    rand = random.randint(0,3)
    photo_path = './photos/edik' + str(rand) + '.jpg'
    bot.send_photo(message.chat.id, open(photo_path, 'rb'))

# бесконечное выполнение кода
bot.polling(none_stop=True, interval=0)