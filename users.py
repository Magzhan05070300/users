import os
from flask import Flask, request
import sqlite3
import telebot
from telebot import types
from github import Github

TOKEN = '5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE'
APP_URL = f'https://jenpulineochered.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

g = Github("magzhan.iitu.kz@mail.ru", "Qwerty1201199445")
repo = g.get_repo("Magzhan05070300/users")
#contents = repo.get_contents("db/database.db")

repo.conn = sqlite3.connect("db/database.db")
cursor = repo.conn.cursor()

def db_table_val1(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_1 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    repo.conn.commit()

#file = repo.get_content("database.db")
#branch = repo.get_branch(branch="main")
"""
user = g.get_user()
repo = g.get_repo()
repo = g.get_repo("users")
contents = repo.get_contents("database.db", ref="database", branch="main")"""


@bot.message_handler(commands=['start'])
def first(message):
    bot.send_message(message.chat.id, 'Сәлеметсіз бе!')
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username

    db_table_val1(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

    id_input = us_id
    cursor.execute("SELECT id FROM db_f_1 WHERE user_id=?", (id_input,))

    for result in cursor:
        bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
        bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
           
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
