import os
from flask import Flask, request
import telebot
from telebot import types
import mysql.connector

TOKEN = '5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE'
APP_URL = f'https://jenpulineochered.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

conn = mysql.connector.connect(host="194.39.67.215", user="jelastic-5256352", password="O60BFWSCBLbn4yJJiWJ3",
                               database='mydb', auth_plugin='mysql_native_password')
cursor = conn.cursor()

"""============================DATABASE========================================================================"""


def db_table_val1(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT IGNORE INTO db_f_1 (user_id, user_name, user_surname, username) VALUES (%s, %s, %s, %s)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val2(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT IGNORE INTO db_f_2 (user_id, user_name, user_surname, username) VALUES (%s, %s, %s, %s)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val3(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT IGNORE INTO db_f_3 (user_id, user_name, user_surname, username) VALUES (%s, %s, %s, %s)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val4(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT IGNORE INTO db_f_4 (user_id, user_name, user_surname, username) VALUES (%s, %s, %s, %s)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val5(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT IGNORE INTO db_f_5 (user_id, user_name, user_surname, username) VALUES (%s, %s, %s, %s)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val6(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT IGNORE INTO db_f_6 (user_id, user_name, user_surname, username) VALUES (%s, %s, %s, %s)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val7(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT IGNORE INTO db_f_7 (user_id, user_name, user_surname, username) VALUES (%s, %s, %s, %s)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


"""==============================================DATABASE_FINISH==================================================="""

Fakultet1 = "Педагогика және психология институты"
Fakultet2 = "Қазақ тілі және әлем тілдері институты"
Fakultet3 = "Физика, математика және цифрлық \nтехнологиялар институты"
Fakultet4 = "Жаратылыстану институты"
Fakultet5 = "Әлеуметтік, гуманитарлық ғылымдар \nжәне өнер институты"
Fakultet6 = "Университет құрамындағы кәсіптік \nбілім беру колледжі"
Fakultet7 = "Магистратура және Докторантура"

kezekInBtn = "Кезекке тұру"
kezekOutBtn = "Кезектен шығу"
homePage = "Бастапқы бетке оралу"
showKezek = "Нөмір қабылдануда!"
"""
g = Github("magzhan.iitu.kz@mail.ru", "Qwerty1201199445")
repo = g.get_repo("Magzhan05070300/users")
contents = repo.get_contents("db/database.sql")"""


@bot.message_handler(commands=['start'])
def first(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add('Мәзір')
    send = bot.send_message(message.chat.id,
                            'Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Мәзірді басып, '
                            'өз факультетіңізді таңдаңыз!',
                            reply_markup=keyboard)
    bot.register_next_step_handler(send, second)


def second(message):
    if message.text == 'Мәзір':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(Fakultet1)
        keyboard.add(Fakultet2)
        keyboard.add(Fakultet3)
        keyboard.add(Fakultet4)
        keyboard.add(Fakultet5)
        keyboard.add(Fakultet6)
        keyboard.add(Fakultet7)
        send = bot.send_message(message.chat.id, 'Таңдаңыз!', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    else:
        bot.send_message(message.chat.id, 'Төменде орналасқан \nмәзірдегі батырманы басыңыз')


@bot.message_handler(content_types=['text'])
def third(message):
    """===============================Fakultetter==================================================="""
    # =================================FAKULTET_1========================================================
    if message.text == Fakultet1:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf1)

    elif message.text == Fakultet2:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf2)

    elif message.text == Fakultet3:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf3)

    elif message.text == Fakultet4:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf4)

    elif message.text == Fakultet5:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf5)

    elif message.text == Fakultet6:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf6)

    elif message.text == Fakultet7:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf7)
    # =================================FAKULTET_2========================================================

    """=================================FINISH======================================================"""
    """===============================Fakultetter==================================================="""


def fakultetf1(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val1(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
        conn.commit()
        id_input = us_id
        cursor.execute("SELECT id FROM db_f_1 WHERE user_id='%s';" % id_input)
        conn.commit()
        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
            conn.commit()
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf1)

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_1''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf1)

        else:
            cursor.execute("SELECT id FROM db_f_1 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Қабылдануда: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf1)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_1 WHERE user_id='%s';" % id_input)
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf1)

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                'Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Мәзірді басып, '
                                'өз факультетіңізді таңдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second)
    """=================================FINISH======================================================"""
    """===============================Fakultetter==================================================="""


def fakultetf2(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val2(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_2 WHERE user_id='%s';" % id_input)

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf2)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_2''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf2)

        else:
            cursor.execute("SELECT id FROM db_f_2 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Қабылдануда: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf2)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_2 WHERE user_id='%s';" % id_input)
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf2)

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                'Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Мәзірді басып, '
                                'өз факультетіңізді таңдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second)


def fakultetf3(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val3(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_3 WHERE user_id='%s';" % id_input)

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf3)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_3''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf3)

        else:
            cursor.execute("SELECT id FROM db_f_3 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Қабылдануда: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf3)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_3 WHERE user_id='%s';" % id_input)
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf3)

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                'Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Мәзірді басып, '
                                'өз факультетіңізді таңдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second)


def fakultetf4(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val4(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_4 WHERE user_id='%s';" % id_input)

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf4)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_4''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf4)

        else:
            cursor.execute("SELECT id FROM db_f_4 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Қабылдануда: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf4)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_4 WHERE user_id='%s';" % id_input)
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf4)

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                'Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Мәзірді басып, '
                                'өз факультетіңізді таңдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second)


def fakultetf5(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val5(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_5 WHERE user_id='%s';" % id_input)

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf5)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_5''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf5)

        else:
            cursor.execute("SELECT id FROM db_f_5 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Қабылдануда: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf5)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_5 WHERE user_id='%s';" % id_input)
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf5)

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                'Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Мәзірді басып, '
                                'өз факультетіңізді таңдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second)


def fakultetf6(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val6(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_6 WHERE user_id='%s';" % id_input)

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf6)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_6''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf6)

        else:
            cursor.execute("SELECT id FROM db_f_6 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Қабылдануда: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf6)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_6 WHERE user_id='%s';" % id_input)
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf6)

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                'Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Мәзірді басып, '
                                'өз факультетіңізді таңдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second)


def fakultetf7(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val7(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_7 WHERE user_id='%s';" % id_input)

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf7)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_7''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf7)

        else:
            cursor.execute("SELECT id FROM db_f_7 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Қабылдануда: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetf7)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_7 WHERE user_id='%s';" % id_input)
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - - - - - - ', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetf7)

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                'Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Мәзірді басып, '
                                'өз факультетіңізді таңдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second)


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
