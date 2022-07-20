import os
from flask import Flask, request
import sqlite3
import telebot
from telebot import types

TOKEN = '5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE'
APP_URL = f'https://jenpulineochered.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

"""============================DATABASE========================================================================"""


def db_table_val1(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_1 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val2(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_2 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val3(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_3 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val4(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_4 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val5(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_5 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val6(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_6 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val7(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_7 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val8(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_8 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val9(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_9 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val10(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_10 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def db_table_val11(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO db_f_11 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


"""==============================================DATABASE_FINISH==================================================="""

Fakultet1 = "1️⃣ Сикинбаев Бауыржан"
Fakultet2 = "2️⃣ Таипова Зульфия"
Fakultet3 = "3️⃣ Орынбай Жансила"
Fakultet4 = "4️⃣ Камысбаева Алия"
Fakultet5 = "5️⃣ Алиева Жанат"
Fakultet6 = "6️⃣ Шәмішова Айбану"
Fakultet7 = "7️⃣ Чаргынова Гульзада"
Fakultet8 = "8️⃣ Бектемір Ақнұр"
Fakultet9 = "9️⃣ Ниязақынов Ердос"
Fakultet10 = "1️⃣0️⃣ Бейсенбаева Назерке"
Fakultet11 = "1️⃣1️⃣ Әбділла Мағжан"
TekseruBtn = "📟Тексеру📟"

kezekInBtn = "Кезекке тұру"
kezekOutBtn = "Кезектен шығу"
showKezek = "Келесі қабылданады!"

homePage = "/start"
homePage2 = "/restartkezek"

kelesi = "Келесі"

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def first(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add('Мәзір')
    send = bot.send_message(message.chat.id,
                            u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                     'В020 Арнайы педагогика\n'
                                     'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                     u'2️⃣' + '*Таипова Зульфия*\n'
                                              'В001 Педагогика және психология\n'
                                              'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                              'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                              'В041 Психология\n\n'
                                              u'3️⃣' + '*Орынбай Жансила*\n'
                                                       'В009 Математика мұғалімдерін даярлау\n'
                                                       'В010 Физика мұғалімдерін даярлау\n'
                                                       'В011 Информатика мұғалімдерін даярлау\n'
                                                       'В054 Физика\n'
                                                       'В057 Ақпараттық технологиялар\n\n'
                                                       u'4️⃣' + '*Камысбаева Алия*\n'
                                                                'В091 Туризм\n'
                                                                'В013 Биология мұғалімдерін даярлау\n'
                                                                'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                'В012 Химия мұғалімдерін даярлау\n'
                                                                'В053 Химия\n'
                                                                'В014 География мұғалімдерін даярлау\n\n'
                                                                u'5️⃣' + '*Алиева Жанат*\n'
                                                                         'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                         'В037 Филология\n'
                                                                         'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                         'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                         u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                  'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                  u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                           'В038 Әлеуметтану\n'
                                                                                           'В090 Әлеуметтік жұмыс\n'
                                                                                           'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                           'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                           'В034 Тарих және археология\n'
                                                                                           'В014 География мұғалімдерін даярлау\n'
                                                                                           'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                           u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                    'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                    'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                    'В028 Хореография\n'
                                                                                                    'В092 Тынығу\n\n'
                                                                                                    u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                             'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                             u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                         'Кәсіби білім беру колледжі\n\n'
                                                                                                                         u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                     'Магистратура және докторантура\n\n'
                                                                                                                                     '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                     'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                            parse_mode='Markdown', reply_markup=keyboard)
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
        keyboard.add(Fakultet8)
        keyboard.add(Fakultet9)
        keyboard.add(Fakultet10)
        keyboard.add(Fakultet11)
        send = bot.send_message(message.chat.id, 'Таңдаңыз!', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second)


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
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF1)

    elif message.text == Fakultet2:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF2)

    elif message.text == Fakultet3:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF3)

    elif message.text == Fakultet4:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF4)

    elif message.text == Fakultet5:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF5)

    elif message.text == Fakultet6:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF6)

    elif message.text == Fakultet7:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF7)

    elif message.text == Fakultet8:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF8)

    elif message.text == Fakultet9:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF9)

    elif message.text == Fakultet10:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF10)

    elif message.text == Fakultet11:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id,
                                'Кезек батырмасын басып, кезекке тұрсаңаз болады!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF11)


    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second)

    # =================================FAKULTET_2========================================================

    """=================================FINISH======================================================"""
    """===============================Fakultetter==================================================="""


def fakultetF1(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val1(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_1 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF1)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF1)

        else:
            cursor.execute("SELECT id FROM db_f_1 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF1)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_1 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF1)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF1)
    """=================================FINISH======================================================"""

    """===============================Fakultetter==================================================="""


def fakultetF2(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val2(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_2 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF2)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF2)

        else:
            cursor.execute("SELECT id FROM db_f_2 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF2)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_2 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF2)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF2)


def fakultetF3(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val3(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_3 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF3)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF3)

        else:
            cursor.execute("SELECT id FROM db_f_3 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF3)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_3 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF3)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF3)


def fakultetF4(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val4(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_4 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF4)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF4)

        else:
            cursor.execute("SELECT id FROM db_f_4 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF4)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_4 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF4)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF4)


def fakultetF5(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val5(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_5 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF5)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF5)

        else:
            cursor.execute("SELECT id FROM db_f_5 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF5)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_5 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF5)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF5)


def fakultetF6(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val6(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_6 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF6)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF6)

        else:
            cursor.execute("SELECT id FROM db_f_6 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF6)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_6 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF6)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF6)


def fakultetF7(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val7(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_7 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF7)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF7)

        else:
            cursor.execute("SELECT id FROM db_f_7 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF7)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_7 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF7)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF7)


def fakultetF8(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val8(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_8 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF8)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_8''')
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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF8)

        else:
            cursor.execute("SELECT id FROM db_f_8 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF8)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_8 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF8)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF8)


def fakultetF9(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val9(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_9 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF9)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_9''')
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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF9)

        else:
            cursor.execute("SELECT id FROM db_f_9 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF9)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_9 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF9)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF9)


def fakultetF10(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val10(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_10 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF10)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_10''')
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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF10)

        else:
            cursor.execute("SELECT id FROM db_f_10 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF10)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_10 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF10)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF10)


def fakultetF11(message):
    if message.text == kezekInBtn:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val11(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        id_input = us_id
        cursor.execute("SELECT id FROM db_f_11 WHERE user_id=?", (id_input,))

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF11)

        for result in cursor:
            print(result[0])

            bot.send_message(message.chat.id, 'Сіздің кезегіңіз қабылданды!')
            bot.send_message(message.chat.id, "Кезек нөмірі: " + str(result[0]))
        conn.commit()

    elif message.text == showKezek:
        cursor.execute('''SELECT COUNT(*) FROM db_f_11''')
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
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF11)

        else:
            cursor.execute("SELECT id FROM db_f_11 LIMIT 1")
            for results in cursor:
                print(results[0])
                bot.send_message(message.chat.id, "Келесі қабылданатын нөмір: " + str(results[0]))
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kezekInBtn)
            keyboard.add(showKezek)
            keyboard.add(kezekOutBtn)
            keyboard.add(homePage)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, fakultetF11)
    elif message.text == kezekOutBtn:
        us_id = message.from_user.id
        id_input = us_id
        cursor.execute("DELETE FROM db_f_11 WHERE user_id=?", (id_input,))
        conn.commit()
        bot.send_message(message.chat.id, "Кезектен шықтыңыз!")
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kezekInBtn)
        keyboard.add(showKezek)
        keyboard.add(kezekOutBtn)
        keyboard.add(homePage)
        send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
        bot.register_next_step_handler(send, fakultetF11)
        conn.commit()

        # =====================================HOME PAGE==========================================================
    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, fakultetF11)


"""--------------------------A---D--M--I--N----------------------------------------------------"""


@bot.message_handler(commands=['restartkezek'])
def firstadmin(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add('Мәзір')
    send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                             'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                            parse_mode='Markdown', reply_markup=keyboard)
    bot.register_next_step_handler(send, secondadmin)


def secondadmin(message):
    if message.text == 'Мәзір':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(Fakultet1)
        keyboard.add(Fakultet2)
        keyboard.add(Fakultet3)
        keyboard.add(Fakultet4)
        keyboard.add(Fakultet5)
        keyboard.add(Fakultet6)
        keyboard.add(Fakultet7)
        keyboard.add(Fakultet8)
        keyboard.add(Fakultet9)
        keyboard.add(Fakultet10)
        keyboard.add(Fakultet11)
        keyboard.add(TekseruBtn)
        send = bot.send_message(message.chat.id, 'Таңдаңыз!', reply_markup=keyboard)
        bot.register_next_step_handler(send, thirdadmin)

    elif message.text == homePage:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id,
                                u'1️⃣' + '*Сикинбаев Бауыржан*\n'
                                         'В020 Арнайы педагогика\n'
                                         'В002 Мектепке дейінгі оқыту және тәрбиелеу\n\n'
                                         u'2️⃣' + '*Таипова Зульфия*\n'
                                                  'В001 Педагогика және психология\n'
                                                  'В003 Бастауышта оқыту педагогикасы мен әдістемесі\n'
                                                  'В019 Әлеуметтік педагогика мамандарын даярлау\n'
                                                  'В041 Психология\n\n'
                                                  u'3️⃣' + '*Орынбай Жансила*\n'
                                                           'В009 Математика мұғалімдерін даярлау\n'
                                                           'В010 Физика мұғалімдерін даярлау\n'
                                                           'В011 Информатика мұғалімдерін даярлау\n'
                                                           'В054 Физика\n'
                                                           'В057 Ақпараттық технологиялар\n\n'
                                                           u'4️⃣' + '*Камысбаева Алия*\n'
                                                                    'В091 Туризм\n'
                                                                    'В013 Биология мұғалімдерін даярлау\n'
                                                                    'В050 Биологиялық және сабақтас ғылымдар\n'
                                                                    'В012 Химия мұғалімдерін даярлау\n'
                                                                    'В053 Химия\n'
                                                                    'В014 География мұғалімдерін даярлау\n\n'
                                                                    u'5️⃣' + '*Алиева Жанат*\n'
                                                                             'В016 Қазақ тілі мен әдебиеті мұғалімдерін даярлау\n'
                                                                             'В037 Филология\n'
                                                                             'В043 Кітапхана ісі, ақпараттарды өңдеу және мұрағат ісі\n'
                                                                             'В017 Орыс тілі мен әдебиеті мұғалімдерін даярлау\n\n'
                                                                             u'6️⃣' + '*Шәмішова Айбану*\n'
                                                                                      'В018 Шет тілі мұғалімдерін даярлау\n\n'
                                                                                      u'7️⃣' + '*Чаргынова Гульзада*\n'
                                                                                               'В038 Әлеуметтану\n'
                                                                                               'В090 Әлеуметтік жұмыс\n'
                                                                                               'В008 Құқық және экономика негіздері мұғалімдерін даярлау\n'
                                                                                               'В015 Гуманитарлық пәндер мұғалімдерін даярлау\n'
                                                                                               'В034 Тарих және археология\n'
                                                                                               'В014 География мұғалімдерін даярлау\n'
                                                                                               'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n\n'
                                                                                               u'8️⃣' + '*Бектемір Ақнұр*\n'
                                                                                                        'В006 Музыка мұғалімдерін даярлау\n'
                                                                                                        'В007 Көркем еңбек және сызу мұғалімдерін даярлау\n'
                                                                                                        'В028 Хореография\n'
                                                                                                        'В092 Тынығу\n\n'
                                                                                                        u'9️⃣' + '*Ниязақынов Ердос*\n'
                                                                                                                 'В005 Дене шынықтыру мұғалімдерін даярлау\n\n'
                                                                                                                 u'1️⃣0️⃣' + '*Бейсенбаева Назерке*\n'
                                                                                                                             'Кәсіби білім беру колледжі\n\n'
                                                                                                                             u'1️⃣1️⃣' + '*Әбділла Мағжан*\n'
                                                                                                                                         'Магистратура және докторантура\n\n'
                                                                                                                                         '*Сәлеметсіз бе! Бұл қабылдау комиссиясына кезекке тұру боты! Тізім бойынша  '
                                                                                                                                         'өз мамандығыңызға сәйкес техникалық хатшыны мәзірден басып таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, secondadmin)


def thirdadmin(message):
    """===============================Fakultetter==================================================="""
    # =================================FAKULTET_1========================================================
    if message.text == Fakultet1:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f1)

    elif message.text == Fakultet2:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f2)

    elif message.text == Fakultet3:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f3)

    elif message.text == Fakultet4:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f4)

    elif message.text == Fakultet5:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f5)

    elif message.text == Fakultet6:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f6)

    elif message.text == Fakultet7:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f7)

    elif message.text == Fakultet8:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f8)

    elif message.text == Fakultet9:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f9)

    elif message.text == Fakultet10:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f10)

    elif message.text == Fakultet11:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(kelesi)
        keyboard.add(homePage2)
        send = bot.send_message(message.chat.id,
                                'Келесі батырмасын басып, кезек қабылдаңыз!',
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, second_page_fakultet_f11)



    elif message.text == TekseruBtn:
        cursor.execute('''SELECT COUNT(*) FROM db_f_1''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Сикинбаев Бауыржан: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Сикинбаев Бауыржан: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)

        cursor.execute('''SELECT COUNT(*) FROM db_f_2''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Таипова Зульфия: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Таипова Зульфия: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_3''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Орынбай Жансила: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Орынбай Жансила: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_4''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Камысбаева Алия: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Камысбаева Алия: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_5''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Алиева Жанат: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Алиева Жанат: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_6''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Шәмішова Айбану: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Шәмішова Айбану: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_7''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Чаргынова Гульзада: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Чаргынова Гульзада: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_8''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Бектемір Ақнұр: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Бектемір Ақнұр: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_9''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Ниязақынов Ердос: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Ниязақынов Ердос: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_10''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Бейсенбаева Назерке: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Бейсенбаева Назерке: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


        cursor.execute('''SELECT COUNT(*) FROM db_f_11''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "❌Әбділла Мағжан: студент жоқ!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)
        else:
            bot.send_message(message.chat.id, "✅Әбділла Мағжан: студент бар!")

            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(TekseruBtn)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '✅✅✅✅✅✅✅✅✅', reply_markup=keyboard)
            bot.register_next_step_handler(send, thirdadmin)


    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)


    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, secondadmin)

    """=================================FINISH======================================================"""
    """===============================Fakultetter==================================================="""


def second_page_fakultet_f1(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_1''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f1)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_1 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))
            """==================USER_NAME CHECK FOR EXIST OR NONE======================="""

            cursor.execute("SELECT user_id FROM db_f_1 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 1-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_1 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f1)
        conn.commit()


    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f1)


def second_page_fakultet_f2(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_2''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f2)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_2 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_2 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 2-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_2 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f2)
        conn.commit()


    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f2)


def second_page_fakultet_f3(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_3''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f3)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_3 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_3 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 3-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_3 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f3)
        conn.commit()



    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f3)


def second_page_fakultet_f4(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_4''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f4)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_4 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_4 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 4-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_4 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f4)
        conn.commit()


    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)


    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f4)


def second_page_fakultet_f5(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_5''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f5)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_5 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_5 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 5-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_5 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f5)
        conn.commit()


    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f5)


def second_page_fakultet_f6(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_6''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f6)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_6 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_6 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 6-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_6 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f6)
        conn.commit()


    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)


    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f6)


def second_page_fakultet_f7(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_7''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f7)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_7 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_7 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 7-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_7 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f7)
        conn.commit()


    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)


    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f7)


def second_page_fakultet_f8(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_8''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f8)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_8 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_8 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 8-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_8 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f8)
        conn.commit()


    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f8)


def second_page_fakultet_f9(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_9''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f9)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_9 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_9 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n14-кабинет, 9-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_9 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f9)
        conn.commit()

    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f9)


def second_page_fakultet_f10(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_10''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f10)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_10 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_10 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n2-қабат, 10-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_10 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f10)
        conn.commit()

    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f10)


def second_page_fakultet_f11(message):
    if message.text == kelesi:
        cursor.execute('''SELECT COUNT(*) FROM db_f_11''')
        check_for_null = cursor.fetchall()
        print(check_for_null)
        if check_for_null[0][0] == 0:
            print("Table no contents")
            bot.send_message(message.chat.id, "Кезекте студент жоқ!")
            keyboard = types.ReplyKeyboardMarkup(True, False)
            keyboard.add(kelesi)
            keyboard.add(homePage2)
            send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
            bot.register_next_step_handler(send, second_page_fakultet_f11)
        else:
            """=============================USER ID===================================="""
            cursor.execute("SELECT id FROM db_f_11 LIMIT 1")
            for get_user_id in cursor:
                print(get_user_id[0])
                bot.send_message(message.chat.id, "Кезек нөмірі:  " + str(get_user_id[0]))

            cursor.execute("SELECT user_id FROM db_f_11 LIMIT 1")
            for results in cursor:
                print(results[0])
                # bot.send_message(message.chat.id, results[0])
                """==============API-KEY======================================"""

                api_key = "5497810512:AAFI8DhRu4apgVAdyeID2ppPJSRQ7Oq0UhE"
                bots = telebot.TeleBot(api_key)

                bots.send_message(chat_id=results[0],
                                  text='Сіздің кезегіңіз келді!\n '
                                       '\n2-қабат, 11-терезеге келіңіз!'
                                       '\nКезек уақыты 5 минут!,')
                """==========================================================="""

                cursor.execute("DELETE FROM db_f_11 WHERE user_id=?", (results[0],))
                conn.commit()

                keyboard = types.ReplyKeyboardMarkup(True, False)
                keyboard.add(kelesi)
                keyboard.add(homePage2)
                send = bot.send_message(message.chat.id, '- - - - - - - - - - - - - - -', reply_markup=keyboard)
                bot.register_next_step_handler(send, second_page_fakultet_f11)
        conn.commit()

    elif message.text == '/restartkezek':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add('Мәзір')
        send = bot.send_message(message.chat.id, '*Сәлеметсіз бе! \nБұл қабылдау комиссиясына кезекке қабылдау '
                                                 'боты!\nМәзірді басып, өз факультетіңізді таңдаңыз!*',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, secondadmin)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second_page_fakultet_f11)


"""--------------------------U--S--E--R--------------------------------------------------------"""


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
