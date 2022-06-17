import os
from flask import Flask, request
import telebot

TOKEN = '5287178701:AAGqjOQohzho-G0wl48-zYNBCcRxW9JC_ic'
TOKEN2 = '5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE'
APP_URL = f'https://usersstudentline.herokuapp.com/{TOKEN, TOKEN2}'
bot = telebot.TeleBot(TOKEN)
bot2 = telebot.TeleBot(TOKEN2)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def first(message):
    bot.send_message(message.chat.id, 'Сәлеметсіз бе USER!')

@bot.message_handler(commands=['start'])
def first(message):
    bot2.send_message(message.chat.id, 'Сәлеметсіз бе ADMIN!')


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

@server.route('/' + TOKEN2, methods=['POST'])
def get_message2():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot2.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200
@server.route('/')
def webhook2():
    bot2.remove_webhook()
    bot2.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
