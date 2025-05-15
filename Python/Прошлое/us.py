import telebot
token = '5705912163:AAGERLxo0o0U8fbkT4VPM4bJmnFusIylvUY'

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
# def f(message):
def reap_all_messe(message):
    # print(message.text)
    bot.send_message(message.chat.id, message.text)

bot.polling(non_stop = True)