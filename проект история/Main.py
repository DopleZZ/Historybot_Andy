import json

import telebot

from config import Token

bot = telebot.TeleBot(Token)

with open("database1.json","r",encoding="UTF-8") as read_file:
    database = json.load(read_file)


@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.send_message(message.chat.id,'Здравствуй! Введи интересующий тебя век арабскими цифрами (8-15)')
        
    except :
        bot.send_message(message.chat.id,'Введите дату верно')


@bot.message_handler(content_types=['text'])
def test(message):
    chatmessage = message.text
    try:
        if chatmessage == "11":
            chatmessage = "12"
        popik = database[f'{chatmessage}']
        bot.send_message(message.chat.id, popik)
    except :
        bot.send_message(message.chat.id,'Введите век верно')



bot.polling()