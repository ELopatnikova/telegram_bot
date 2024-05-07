import telebot # Импортируем telebot
import telegram
from telebot import types # для определения типов
from telegram import Bot, InputFile
from secrets import secrets # импортируем словарь с токеном из файла secrets.py

# передаём значение переменной с кодом экземпляру бота
token = ('7062105451:AAEzx21-UAkOEqBDwMuxq9y9eb5LHL-YqTo')
bot = telebot.TeleBot(token)

# хендлер и функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здорова, отец")

# отправка фото
@bot.message_handler(commands=['elenka', 'lena_lopa'])
def name_message(message):
    bot.send_message(message.chat.id, "Ща кину")
    photo_path = './photos/elenka.jpg'
    bot.send_photo(message.chat.id, open(photo_path, 'rb'))

# бесконечное выполнение кода
bot.polling(none_stop=True, interval=0)