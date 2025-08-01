import telebot

# Bu yerga o'zingizning tokeningizni yozing
TOKEN = '8060087878:AAFhS_FggsCzUR20grTZmi398jG5N0oKyrU'

bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Botga xush kelibsiz. 😊")

# Har qanday matnga javob berish
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    text = message.text.lower()

    if "salom" in text:
        bot.reply_to(message, "Salom! Qanday yordam bera olaman?")
    elif "rahmat" in text:
        bot.reply_to(message, "Yaxshi! Yordam kerak bo‘lsa, yozing.")
    else:
        bot.reply_to(message, "Bu haqida aniq ma’lumot yo‘q. /start ni bosing.")

# Botni ishga tushirish
bot.polling()
