import os
from flask import Flask, request
import telebot
import github

TOKEN = '5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE'
APP_URL = f'https://jenpulineochered.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

g = github.Github("magzhan.iitu.kz@mail.ru", "Qwerty1201199445")
user = g.get_user()

"""
user = g.get_user()
repo = g.get_repo()
repo = g.get_repo("users")
contents = repo.get_contents("database.db", ref="database", branch="main")"""

@bot.message_handler(commands=['start'])
def first(message):
    bot.send_message(message.chat.id, 'Сәлеметсіз бе!')


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
