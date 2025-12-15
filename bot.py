import telebot
from telebot import types

TOKEN = "8175254047:AAGnVK73glsuqlF_CLqCzSErVwFtiTJxVmg"
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📜 Манас")
    btn2 = types.KeyboardButton("📘 Семетей")
    btn3 = types.KeyboardButton("📕 Сейтек")
    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "📖 Добро пожаловать!\n\n"
        "Этот бот посвящён эпосу «Манас».\n"
        "Выберите главу:",
        reply_markup=markup
    )

# Обработка кнопок
@bot.message_handler(func=lambda message: True)
def chapters(message):
    if message.text == "📜 Манас":
        bot.send_message(
            message.chat.id,
            "Эпос «Манас»:\n"
            "https://example.com/manas"
        )

    elif message.text == "📘 Семетей":
        bot.send_message(
            message.chat.id,
            "Эпос «Семетей»:\n"
            "https://example.com/semetey"
        )

    elif message.text == "📕 Сейтек":
        bot.send_message(
            message.chat.id,
            "Эпос «Сейтек»:\n"
            "https://example.com/seitek"
        )

    else:
        bot.send_message(
            message.chat.id,
            "Пожалуйста, выберите главу с кнопок 👇"
        )

bot.polling()
