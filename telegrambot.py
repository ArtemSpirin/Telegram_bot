import telebot
from telebot import types
from data import *
bot = telebot.TeleBot('7227822094:AAF8d2eKdzzukxxr2z9-zjzRUgPmDX27Ai0')
# t.me/physics1478_bot

all_markups = {}
global numbers
numbers = [i for i in range(1000)]
values = {}
def send_message(callback, message, section):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(callback.message.chat.id, message, reply_markup=all_markups[section])

def creat_markup(list):
    global numbers
    flag = 0
    if numbers[0] == 0:
        flag = 1
    values = []
    markup = types.InlineKeyboardMarkup()
    inner_counter = {}
    for i in range(len(list)):
        inner_counter.update({list[i]: numbers[0]})
        values.append(numbers[0])
        numbers = numbers[1:]
    for elm in inner_counter:
        markup.add(types.InlineKeyboardButton(elm, callback_data=str(inner_counter.get(elm))))
    if flag == 0:
        markup.add(types.InlineKeyboardButton('Назад', callback_data=numbers[0]))
        values.append(numbers[0])
        numbers = numbers[1:]
    return [markup,values]


def create_final_markups(callback, lections='', solver=None, textbook=None):
    global numbers
    values = []
    markup = types.InlineKeyboardMarkup()
    if lections != '':
        markup.add(types.InlineKeyboardButton('Ютуб леккции', url=lections))
    if solver != None:
        markup.add(types.InlineKeyboardButton('Учебники', callback_data=send_file(callback,solver)))
    if textbook != None:
        markup.add(types.InlineKeyboardButton('Решебники', callback_data=send_file(callback, textbook)))
    markup.add(types.InlineKeyboardButton('Назад', callback_data=numbers[0]))
    values.append(numbers[0])
    numbers = numbers[1:]
    return [markup, values]


for section in subjects:
    list = creat_markup(subjects[section])
    all_markups[section] = list[0]
    values[section] = list[1]
    for section in subjects:
        for elm in subjects[section]:
            create_final_markups()

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=all_markups['general'])

@bot.callback_query_handler(func=lambda callback: True)
def send_file(callback, file):
    bot.send_document(callback.message.chat.id, file)
def choose(callback):
    section = None
    value = 0
    for elm in values:
        if int(callback.data) in values[elm]:
            section = elm
            value = int(callback.data)
    if section == 'general':
        match value:
            case 0:
                send_message(callback,'Выбери тему','physics')
        match value:
            case 1:
                send_message(callback,'Выбери тему','math')
        match value:
            case 2:
                send_message(callback,'Выбери тему','languages')
        match value:
            case 3:
                send_message(callback,'Выбери тему','history')
        match value:
            case 4:
                send_message(callback,'Выбери тему','IT')
    elif section in subjects and values[section][-1] == value:
        send_message(callback,'Выбери предмет','general')
bot.polling(none_stop=True)
