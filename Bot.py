import telebot

TOKEN = "8548437636:AAG0ZNi7Wtof8XjZfgFoaFcptxaMh4Qp3Do"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Halo! Kirim /halo untuk stiker")

@bot.message_handler(commands=['halo'])
def halo(message):
    sticker = "CAACAgUAAxkBAAJo22mgrAwCrpfwqJSzH37tO4UOwrdtAALJGgACpoyZVwpG3R8jGIpFOgQ"
    bot.send_sticker(message.chat.id, sticker)

bot.infinity_polling()
