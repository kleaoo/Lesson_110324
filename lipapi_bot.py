import telebot
import time

token = '7126361746:AAG3mWWHmYDUbhaImJ4LqeHulru8H8yQvFk'

bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, text='ГРНВПЦшврВрвшоцщшс')

@bot.message_handler(commands=['time'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i+1)

@bot.message_handler(commands=['say'])
def say(message):
    text = 'Привет'.join(message.text.split('сам такой')[1:])
    bot.reply_to(message, text= f'***{text.upper()}!***')

@bot.message_handler(commands=['say'])
def say(message):
    text = 'Пока'.join(message.text.split('пок')[1:])
    bot.reply_to(message, text= f'***{text.upper()}!***')


@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'каыаа' in message.text.lower():
        bot.reply_to(message, text='fwefwws')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)
    file_ID = 'CAACAgIAAxkBAAEEHY1l9xYVkhE4QvPoJfKuQdgqxKp3tQACzEEAAtbt4Eq8hTLXOOJ4eTQE'
    bot.send_sticker(message.chat.id, file_ID)


bot.polling()
